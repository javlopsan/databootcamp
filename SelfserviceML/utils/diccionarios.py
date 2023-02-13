
dict_features={'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
 'PaymentMethod': {'Bank transfer': 0,
  'Credit card': 1,
  'Electronic check': 2,
  'Mailed check': 3},
 'gender': {'Female': 0, 'Male': 1},
 'Partner': {'No': 0, 'Yes': 1},
 'Dependents': {'No': 0, 'Yes': 1}}

dict_MultiLine={
                'No': 0,
                'Yes':1,
                'No phone service': 0
                }

dict_ONLServ={
                'No': 0,
                'Yes':1,
                'No internet service': 0
                }


'''temp=df[list_features(df)]
pd.DataFrame({col: temp[col].astype('category').cat.codes for col in temp}, index=temp.index)
dict_features={col: {n: cat for n, cat in zip(temp[col].astype('category').cat.categories,range(len(temp[col])))} 
     for col in temp}'''