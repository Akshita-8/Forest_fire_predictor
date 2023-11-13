import streamlit as str
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

def predict_forest(oxygen,humidity,temperature):
    input=np.array([[oxygen,humidity,temperature]]).astype(np.float64)
    prediction=model.predict_proba(input)
    p='{0:.{1}f}'.format(prediction[0][0],2)
    return float(p)

def main():
    
    main_html = """
    <div style="background-color:#025246;padding:10px">
    <h2 style="color:white;text-align:center;">Forest Fire Prediction</h2>
    </div>
    """
    str.markdown(main_html, unsafe_allow_html=True)
    oxygen = str.text_input("Oxygen")
    humidity = str.text_input("Humidity")
    temperature = str.text_input("Temperature")
    safe_html="""  
      <div style="background-color:#f7b839;text-align:center" >
       <h4>The forest is safe.</h4>
       </div>
    """
    danger_html="""  
      <div style="background-color:#f74036;text-align:center">
       <h4>The forest is in danger.</h4>
       </div>
    """
    mid_html="""  
      <div style="background-color:#f74036;text-align:center">
       <h4>The forest is in a potentially uncertain state.Caution is advised.</h4>
       </div>
    """

    if str.button("PREDICT"):
        result=predict_forest(oxygen,humidity,temperature)
        str.success('The probability of fire taking place is {}'.format(result))

        if(result>0.7):
            str.markdown(danger_html,unsafe_allow_html=True)
        elif(result<0.5):
            str.markdown(safe_html,unsafe_allow_html=True)
        else:
            str.markdown(mid_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
