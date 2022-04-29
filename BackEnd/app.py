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
from models.apple import appleloadedmodel as aapl
from models.apple import applesentimentanalysis as aaplsen
from models.infosys import infosysloadedmodel as infy
from models.infosys import infosyssentimentanalysis as infysen
from models.rel import relianceloadedmodel as rel
from models.rel import reliancesentimentanalysis as relsen
from models.sbi import sbiloadedmodel as sbi
from models.sbi import sbisentimentanalysis as sbisen
from models.tcs import tcsloadedmodel as tcs
from models.tcs import tcssentimentanalysis as tcssen

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

@app.route("/api/apple", methods=['GET'])
@cross_origin()
def indexFive():
    return{
        'aapllstmdata': aapl.applelstmsavedmodel(),
        'aaplarimadata': aapl.applearimamodel(),
        'aapllrdata': aapl.applelinearregression(),
        'aaplsentiment': aaplsen.applesentimentanalysis()
    }

@app.route("/api/infosys", methods=['GET'])
@cross_origin()
def indexSix():
    return{
        'infylstmdata': infy.infosyslstmsavedmodel(),
        'infyarimadata': infy.infosysarimamodel(),
        'infylrdata': infy.infosyslinearregression(),
        'infysentiment': infysen.infosyssentimentanalysis()
    }

@app.route("/api/reliance", methods=['GET'])
@cross_origin()
def indexSeven():
    return{
        'rellstmdata': rel.reliancelstmsavedmodel(),
        'relarimadata': rel.reliancearimamodel(),
        'rellrdata': rel.reliancelinearregression(),
        'relsentiment': relsen.reliancesentimentanalysis()
    }

@app.route("/api/sbi", methods=['GET'])
@cross_origin()
def indexEight():
    return{
        'sbilstmdata': sbi.sbilstmsavedmodel(),
        'sbiarimadata': sbi.sbiarimamodel(),
        'sbilrdata': sbi.sbilinearregression(),
        'sbisentiment': sbisen.sbisentimentanalysis()
    }

@app.route("/api/tcs", methods=['GET'])
@cross_origin()
def indexNine():
    return{
        'tcslstmdata': tcs.tcslstmsavedmodel(),
        'tcsarimadata': tcs.tcsarimamodel(),
        'tcslrdata': tcs.tcslinearregression(),
        'tcssentiment': tcssen.tcssentimentanalysis()
    }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)