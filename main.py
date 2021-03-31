from regression_model import train_model, predict
from sanic import Sanic, response as res

# only run once
train_model()

app = Sanic('app')

# GET /api/predict/:age/:income

# POST /api/predict
# { age, income }

@app.post('/api/predict')
async def predict_click(req):
  values = req.json

  # get prediction with provided values
  prediction = predict(values['age'], values['income'])

  # send prediction as json
  return res.json(prediction)


if __name__ == '__main__':
  app.run(port=5000)
  