from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rate_rf.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method=="POST":
        date_dep=request.form["Dep_Time"]
        Journey_day=int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month=int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        Journey_year=int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").year)

        day=(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M")).weekday()
        Dep_hour=int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        if day==0:
            wdm=1
            wdt=0
            wdw=0
            wdth=0
            wdf=0
            wds=0
            wdsn=0
        elif day==1:
            wdm=0
            wdt=1
            wdw=0
            wdth=0
            wdf=0
            wds=0
            wdsn=0
        elif day==2:
            wdm=0
            wdt=0
            wdw=1
            wdth=0
            wdf=0
            wds=0
            wdsn=0
        elif day==3:
            wdm=0
            wdt=0
            wdw=0
            wdth=1
            wdf=0
            wds=0
            wdsn=0
        elif day==4:
            wdm=0
            wdt=0
            wdw=0
            wdth=0
            wdf=1
            wds=0
            wdsn=0
        elif day==5:
            wdm=0
            wdt=0
            wdw=0
            wdth=0
            wdf=0
            wds=1
            wdsn=0
        elif day==6:
            wdm=0
            wdt=0
            wdw=0
            wdth=0
            wdf=0
            wds=0
            wdsn=1


        if Journey_month=='1':
            Jan=1
            Mar=0
            Apr=0
            May=0
            June=0
            Sep=0
            Dec=0
        elif Journey_month=='3':
            Jan=0
            Mar=1
            Apr=0
            May=0
            June=0
            Sep=0
            Dec=0
        elif Journey_month=='4':
            Jan=0
            Mar=0
            Apr=1
            May=0
            June=0
            Sep=0
            Dec=0
        elif Journey_month=='5':
            Jan=0
            Mar=0
            Apr=0
            May=1
            June=0
            Sep=0
            Dec=0
        elif Journey_month=='6':
            Jan=0
            Mar=0
            Apr=0
            May=0
            June=1
            Sep=0
            Dec=0
        elif Journey_month=='9':
            Jan=0
            Mar=0
            Apr=0
            May=0
            June=0
            Sep=1
            Dec=0
        elif Journey_month=='12':
            Jan=0
            Mar=0
            Apr=0
            May=0
            June=0
            Sep=0
            Dec=1
        else:
            Jan=0
            Mar=0
            Apr=0
            May=0
            June=0
            Sep=0
            Dec=0



        if Dep_hour >= 0 and Dep_hour < 6:
            ft_mn=1
            ft_mr=0
            ft_af=0
            ft_ev=0
        elif Dep_hour >= 6 and Dep_hour < 12:
            ft_mn=0
            ft_mr=1
            ft_af=0
            ft_ev=0
        elif Dep_hour >= 12 and Dep_hour < 18:
            ft_mn=0
            ft_mr=0
            ft_af=1
            ft_ev=0
        elif Dep_hour >= 18 and Dep_hour < 24:
            ft_mn=0
            ft_mr=0
            ft_af=0
            ft_ev=1
        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        Dur = dur_hour*60 + dur_min
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']

        if(airline=='Jet Airways'):
            Jet_Airways = 1
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0

        elif (airline=='Air India'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0 
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Another = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy' or airline=='Trujet'):
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 1
            
        else:
            Jet_Airways = 0
            Air_Asia = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Another = 0

        print(Jet_Airways,
            IndiGo,
            Air_India,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            GoAir,
            Multiple_carriers_Premium_economy,
            Jet_Airways_Business,
            Another)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Banglore = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Banglore = 0

        elif (Source == 'Banglore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai,
        #     s_Banglore)

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0

        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_Banglore = 0

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_Banglore = 0
        
        elif (Destination == 'Banglore'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0
        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata,
        #     d_Banglore
        # )

        add_info=request.form["AddInfo"]
        if add_info=='1 Long layover':
            ll_1=1
            sl_1=0
            ll_2=0
            bc=0
            ca=0
            mnot=0
            ni=0
            cib=0
            ref=0
        elif add_info=='1 Short layover':
            ll_1=0
            sl_1=1
            ll_2=0
            bc=0
            ca=0
            mnot=0
            ni=0
            cib=0
            ref=0
        elif add_info=='2 Long layover':
            ll_1=0
            sl_1=0
            ll_2=1
            bc=0
            ca=0
            mnot=0
            ni=0
            cib=0
            ref=0
        elif add_info=='Business class':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=1
            ca=0
            mnot=0
            ni=0
            cib=0
            ref=0
        elif add_info=='Change airports':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=0
            ca=1
            mnot=0
            ni=0
            cib=0
            ref=0
        elif add_info=='In-flight meal not included':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=0
            ca=0
            mnot=1
            ni=0
            cib=0
            ref=0
        elif add_info=='No Info':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=0
            ca=0
            mnot=0
            ni=1
            cib=0
            ref=0
        elif add_info=='No check-in baggage included':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=0
            ca=0
            mnot=0
            ni=0
            cib=1
            ref=0
        elif add_info=='Red-eye flight':
            ll_1=0
            sl_1=0
            ll_2=0
            bc=0
            ca=0
            mnot=0
            ni=0
            cib=0
            ref=1
            


        
        prediction=model.predict([[
            Dur,
            Total_stops,
            Journey_year,
            Journey_day,
            Air_Asia,
            Air_India,
            Another,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Vistara,
            s_Banglore,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Banglore,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi,
            ll_1,
            sl_1,
            ll_2,
            bc,
            ca,
            mnot,
            ni,
            cib,
            ref,
            ft_af,
            ft_ev,
            ft_mn,
            ft_mr,
            Jan,
            Mar,
            Apr,
            May,
            June,
            Sep,
            Dec,
            wdf,
            wdm,
            wdsn,
            wds,
            wdth,
            wdt,
            wdw
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

# import pandas as pd
# d="2021-03-03 13:40"
# Journey_day = int(pd.to_datetime(d, format="%Y-%m-%dT%H:%M").day)
# Journey_month = int(pd.to_datetime(d, format ="%Y-%m-%dT%H:%M").month)
# Journey_hour = int(pd.to_datetime(d, format ="%Y-%m-%dT%H:%M").hour)
# Journey_minute = int(pd.to_datetime(d, format ="%Y-%m-%dT%H:%M").minute)
# day=(pd.to_datetime(d, format="%Y-%m-%dT%H:%M")).weekday()

# print(type(Journey_day))
# print(Journey_month)
# print(Journey_hour)
# print(Journey_minute)
# print((day))