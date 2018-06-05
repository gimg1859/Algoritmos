from quantopian.algorithm import (
    attach_pipeline,
    pipeline_output,
    order_optimal_portfolio,
)
import quantopian.algorithm as algo
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage
from quantopian.pipeline.filters import Q1500US
from quantopian.pipeline.filters import  StaticAssets
import quantopian.optimize as opt
from quantopian.pipeline.experimental import risk_loading_pipeline
from quantopian.optimize import TargetWeights
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from collections import deque
def initialize(context):
    # SPY capital, EFA fondos, TIP bonos, GSG indince. 
    context.security_list = symbols('SPY', 'EFA','TIP','GSG')
    context.classifier = KNeighborsClassifier(n_neighbors=7, weights='uniform', algorithm='kd_tree') # Usar un clasificador KNN
    
   #Parametros de restriccion   
    # Attach de pileine datos
    attach_pipeline(
        make_pipeline(),
        'data_pipe'
    )
    
    attach_pipeline(
        risk_loading_pipeline(),
        'risk_pipe'
    )

    # Rebalance 2 horas de abrir el mercado
    algo.schedule_function(
        rebalance,
        algo.date_rules.month_end(),
        algo.time_rules.market_open(hours=2),
    )

    # guardar al cierre todos los dias
    algo.schedule_function(
        record_vars,
        algo.date_rules.every_day(),
        algo.time_rules.market_close()
    )

    # crea el conjunto seleccionado
    algo.attach_pipeline(make_pipeline(), 'pipeline')

def make_pipeline():
  #mencionados anteriormente
    base_universe =  StaticAssets(symbols('SPY', 'EFA','TIP','GSG'))
    
    # precio de cierre del dia anterior
    yesterday_close = USEquityPricing.close.latest
    sma_25 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=25)   # Variables independientes
    sma_200 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=200) # Variables dependientes 
    pipe = Pipeline(
        screen=base_universe & (sma_25 > sma_200),
        columns={
            'price': yesterday_close,
            'sma_200': sma_200,
        }
    )
     
    return pipe
def before_trading_start(context, data):

    context.output = algo.pipeline_output('pipeline')
    #Lo que se va a negociar
    #context.security_list = context.output.index
    log.info(context.security_list)
    context.risk_factor_betas = pipeline_output('risk_pipe')
    #securities a comerciar
    context.securities_for_month = context.output.index
    context.weights =  pd.Series([.25, .25, .25, .25],
                         index = context.security_list)
    context.prediction = 0 # Se guarda la predicción más reciente

def rebalance(context, data):
#se ejecuta de acuerdo a schedule_fuction
    log.info(context.output.head(10))
        context.recent_prices.append(data.current(context.security, 'price')) # Agrega el precio actual a la cola
    weights = {}
    #context.security_list = symbols('SPY', 'EFA','TIP','GSG')
    for equity in context.security_list:
        #comprueba si el capital del pipeline para el mes y asignar peso
        if(context.securities_for_month.any(equity)):
            #weights[equity] =  float(context.weights[equity])
            weights[equity] =  .20
        else:
            # Trade if there is more than a 1% decrease (SHORT)
            weights[equity] = -1 * context.weights[equity]

    log.info("context weights %s" %context.weights)
    # optimizate api contest
    objective = opt.TargetWeights(weights)
    order_optimal_portfolio(objective, [opt.MaxGrossExposure(1)])
    if len(context.recent_prices) == context.window_length+2: # Garantiza que hayan datos suficientes para generar un buen modelo
   # opt.order_optimal_portfolio(objective=TargetWeights(context.weights),constraints=[])
    # Hace una lista de booleanos para saber si los precios han cambiado respecto a los anteriores
        changes = np.diff(context.recent_prices) > 0
        sma_25.append(changes[:-1]) # Variables independientes
        sma_200.append(changes[-1]) # Variables dependientes

        if len(sma_200) >= 100: # Garantiza que hayan datos suficientes para generar un buen modelo
                
            context.classifier.fit(context.X, context.Y) # Generar el modelo
            
            context.prediction = context.classifier.predict(changes[1:]) # Predicción
            
            # Si la predicción es True, se compran todas las acciones posibles, si es False, se venden todas las acciones posibles del portafolio
            order_target_percent(context.security, context.prediction)        
    # tiene el tiempo de cambio actual 
    exchange_time = get_datetime('US/Eastern')
def record_vars(context, data):
    record(prediction=int(context.prediction))