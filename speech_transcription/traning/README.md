CTC and LSTM Sample [here](https://github.com/dmlc/mxnet/tree/master/example/warpctc).

### Generating data

Run `generate_data.py` in `generate_data`. When generating training and test data, please remember to change output path and number in `generate_data.py`

### Train the model

1. LSTM

```
python train_lstm.py
```

You can do the prediction using your trained model.

```
python lstm_predictor.py
```



