# rl-trade

## On colab 
1. Single Stock Trading and Backtesting:- [notebook](https://colab.research.google.com/drive/19jt1DXyL3Z2yP9vePaDRvLb1CYNBYtNG?usp=sharing)
2. Portfolio Stock Trading and Backtesting: [notebook](https://colab.research.google.com/drive/1kMvRYkM9HcwGMYNnskoh4hM14OAkSEwL?usp=sharing)
3. Ensemble Stock Trading and Backtesting: [notebook](https://colab.research.google.com/drive/1Fc5H1Qv1HO6DjN3KJFp6fHkFE4hfreYV#scrollTo=5CwpyIwZG1w0) (work in progress)

## On Local Machine (Os: ubuntu-linux)

### Python 3.7.11 or greater is required
    conda create -n env_name python=3.7
    conda activate env_name

### pip install for testing.
    pip install rltrade-test
 
#### Import
```python
from rltrade import config
from rltrade.models import DRLAgent
from rltrade.environments import StockTradingEnv
from rltrade.backtests import backtest_plot,backtest_stats
from rltrade.data import FeatureEngineer,YahooDownloader
```
#### Downloading data
```python
ticker = config.FAANG_TICKER_DICT['apple']

print('Downloading Data')
df = YahooDownloader(start_date = '2009-01-01',
                        end_date = '2021-01-01',
                        ticker_list = ticker).fetch_data()

print("Preprocessing data")
train_period = ('2009-01-01','2019-01-01')
test_period = ('2019-01-01','2021-01-01')

fe = FeatureEngineer(stock_indicators=True,
                    turbulence=True,
                    stock_indicator_list=config.STOCK_INDICATORS_LIST)

train,trade = fe.train_test_split(df,train_period,test_period)
```
#### Setting up Environment

```python
env_kwargs = {
    "hmax": 100, 
    "initial_amount": 100000, 
    "buy_cost_pct": 0.001, 
    "sell_cost_pct":0.001,
    "tech_indicator_list": config.STOCK_INDICATORS_LIST, 
    "reward_scaling": 1e-4}

e_train_gym = StockTradingEnv(df=train,**env_kwargs)
env_train, _ = e_train_gym.get_sb_env()

e_trade_gym = StockTradingEnv(df=trade,**env_kwargs)
env_trade,obs_trade = e_trade_gym.get_sb_env()

```
#### Training model and trading

```python
agent = DRLAgent(env = env_train)
PPO_PARAMS = {'n_steps':2048,
            'ent_coef':0.005,
            'learning_rate':0.0001,
            'batch_size':128}

model_ppo = agent.get_model("ppo",model_kwargs=PPO_PARAMS)

trained_ppo = agent.train_model(model=model_ppo,
                                tb_log_name='ppo',
                                total_timesteps=5000)

df_account_value,df_actions = DRLAgent.DRL_prediction(model=trained_ppo,
                                                        environment=e_trade_gym)
```
#### Backtesting using pyfolio

```python
perf_stats_all = backtest_stats(account_value=df_account_value)
backtest_plot(account_value=df_account_value,
        baseline_ticker='AAPL',
        baseline_start = '2019-01-01', 
        baseline_end = '2021-01-01')

```

