from flask import Flask
from flask import jsonify

#for cors
from flask_cors import CORS, cross_origin

#import models
from models.msft import microsoftloadedmodel as msft
from models.msft import msftsentimentanalysis as msftsen
from models.google import googleloadedmodel as goog
from models.google import googlesentimentanalysis as googsen
from models.amazon import amazonloadedmodel as amzn
from models.amazon import amazonsentimentanalysis as amznsen
from models.icici import iciciloadedmodel as icici
from models.icici import icicisentimentanalysis as icicisen

app = Flask(__name__)
cors = CORS(app)


@app.route("/api/microsoft", methods = ['GET'])
@cross_origin()
def index():
    return{
        'msftlstmdata': msft.msftlstmsavedmodel(),
        'msftarimadata': msft.msftarimamodel(),
        'msftlrdata': msft.msftlinearregression(),
        'msftsentiment': msftsen.msftsentimentanalysis()
    }

@app.route("/api/google", methods=['GET'])
@cross_origin()
def indexTwo():
    return{
        'googlstmdata': goog.googlelstmsavedmodel(),
        'googarimadata': goog.googlearimamodel(),
        'googlrdata': goog.googlelinearregression(),
        'googsentment': googsen.googlesentimentanalysis()
    }

@app.route("/api/amazon", methods=['GET'])
@cross_origin()
def indexThree():
    return{
        'amznlstmdata': amzn.amazonlstmsavedmodel(),
        'amznarimadata': amzn.amazonarimamodel(),
        'amznlrdata': amzn.amazonlinearregression(),
        'amznsentiment': amznsen.amazonsentimentanalysis()
    }

@app.route("/api/icici", methods=['GET'])
@cross_origin()
def indexFour():
    return{
        'icicilstmdata': icici.icicilstmsavedmodel(),
        'iciciarimadata': icici.iciciarimamodel(),
        'icicilrdata': icici.icicilinearregression(),
        'icicisentiment': icicisen.icicisentimentanalysis()
    }

if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)