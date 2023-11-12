import streamlit as str
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_forest(oxygen,humidity,temperature):
    input=np.array([[oxygen,humidity,temperature]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Forest Fire Prediction</h2>
    </div>
    """
    str.markdown(html_temp, unsafe_allow_html=True)

    oxygen = str.text_input("Oxygen")
    humidity = str.text_input("Humidity")
    temperature = str.text_input("Temperature")
    safe_html="""  
      <div style="background-color:#f7b839;text-align:center" >
       <h4> Your forest is Safe</h4>
       </div>
    """
    danger_html="""  
      <div style="background-color:#f74036;text-align:center">
       <h4> Your forest is in Danger</h4>
       </div>
    """

    if str.button("Predict"):
        output=predict_forest(oxygen,humidity,temperature)
        str.success('The probability of fire taking place is {}'.format(output))

        if output > 0.5:
            str.markdown(danger_html,unsafe_allow_html=True)
        else:
            str.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()