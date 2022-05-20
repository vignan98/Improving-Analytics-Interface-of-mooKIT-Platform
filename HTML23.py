import pymongo
import dash
import plotly.graph_objs as go
import plotly.plotly as py
import dash_core_components as dcc
import dash_html_components as html
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["analytics_relativity"]
col=db["userInfo"]
query={"Qualification":{"$exists":"true"},"Gender":{"$exists":"true"}}
doc=col.find(query)
Countries=[]
array=[]
check=[]
for x in doc:
	if x["Country"] not in Countries:
		Countries.append(x["Country"])
app=dash.Dash()
app.layout=html.Div([
	dcc.Tabs(id='tabs-example',value='tab-1-example',children=[
	dcc.Tab(label='Summary',value='tab-1-example'),
	dcc.Tab(label='Registrations',value='tab-2-example',children=[
		html.Div("Filter by  Educational Qualification::",style={'fontSize':25}),
		dcc.Dropdown(
		id='Qualification',
		options=[
			{'label':'All Qualifications','value':'All Qualifications'},
			{'label': 'Post Graduate', 'value': 'Post Graduate'},
			{'label': 'Under Graduate', 'value': 'Under Graduate'},
			{'label': 'Doctorate','value':'Doctorate'},
			{'label':'Others','value':'Others'},
			{'label':'High School','value':'High School'},
			{'label':'Pre University','value':'Pre University'},
			{'label':'Not Disclosed','value':'Not Disclosed'}
		],
		value='All Qualifications',
		style={'height':'30px','width':'300px','display':'inline-block'}
		),
		html.Br(),
		html.Br(),
		html.Div("Filter by  Gender:",style={'fontSize':25}),
		dcc.RadioItems(
		id='Gender',
		options=[
			{'label': 'Male', 'value': 'Male'},
			{'label': 'Female', 'value': 'Female'},
			{'label':'Both Genders','value':'Both Genders'}
		],
		value='Both Genders',
		labelStyle={'display':'block','cursor':'pointer','margin-left':'20px'},
		style={'fontSize':25,'padding-top':'20px'}
		),
		html.Br(),
		html.Div("Filter by  Affiliation",style={'fontSize':25}),
		dcc.Dropdown(
		id='Affiliation',
		options=[
			{'label':'All Affiliations','value':'All Affiliations'},
			{'label':'Individual','value':'Individual'},
			{'label':'Academia','value':'Academia'},
			{'label':'Non-profit organization','value':'Non-profit organization'},
			{'label':'For-profit organization','value':'For-profit organization'},
			{'label':'Community organization','value':'Community organization'}
		],
		value='All Affiliations',
		style={'height':'30px','width':'300px','display':'inline-block'}
		),
		html.Br(),
		html.Br(),
		html.Div("Filter by  AgeGroup:",style={'fontSize':25}),
		dcc.Dropdown(
		id='ageGroup',
		options=[
			{'label':'all ageGroups','value':'All ageGroups'},
			{'label': 'less than 16', 'value': 'less than 16'},
			{'label': '16-20', 'value': '16-20'},
			{'label': '21-25','value':'21-25'},
			{'label':'26-30','value':'26-30'},
			{'label':'31-35','value':'31-35'},
			{'label':'36-40','value':'36-40'},
			{'label':'41-45','value':'41-45'},
			{'label':'45-50','value':'46-50'},
			{'label':'greater than 50','value':'greater than 50'}
		],
		value='All ageGroups',
		style={'height':'30px','width':'300px','display':'inline-block'}
		),
	]),
	dcc.Tab(label='Results',value='tab-3-example'),
	dcc.Tab(label='Views',value='tab-4-example')]),
	html.Div(id='tabs-content-example'),
	html.Br(),
	html.Br(),
	html.Br()
])
@app.callback(
	dash.dependencies.Output('tabs-content-example','children'),
	[dash.dependencies.Input('tabs-example','value'),
	dash.dependencies.Input('Qualification','value'),
	dash.dependencies.Input('Gender','value'),
	dash.dependencies.Input('Affiliation','value'),
	dash.dependencies.Input('ageGroup','value')])
def button_click(tab,selector1,selector2,selector3,selector4):
	count=0
	data1=[]
	data2=[]
	data=[]
	data3=[]
	data4=[]
	i=0
	j=0
	k=0
	v=0
	u=0
	cou=0
	array=[]
	array1=[]
	array2=[]
	array3=[]
	array4=[]
	Gender=['Male','Female']
	Qualification=['Post Graduate','Under Graduate','Doctorate','Pre University','High School','Others','Not Disclosed']
	Affiliation=['Individual','Academia','Non-profit organization','For-profit organization','Community organization']
	AgeGroup=['less than 16','16-20','21-25','26-30','31-35','36-40','41-45','46-50','greater than 50']
	if(tab=='tab-2-example'):
		if((selector1 in Qualification)or(selector2 in Gender) or(selector3 in Affiliation)or(selector4 in AgeGroup)):
			count=count+1
		if((tab=='tab-2-example')and(count==0)):				
			while i in range(len(Countries)) or j in range(len(Qualification))or k in range(len(AgeGroup)) or v in range(len(Affiliation))or u in range(len(Gender)):
				if(i in range(len(Countries))):
					query2={"Country":Countries[i]}
					doc2=col.find(query2,{"Country":1})
					for  t in doc2:
						cou=cou+1
					array.append(cou)
					i=i+1
					cou=0
				if(j in range(len(Qualification))):
					query3={"Qualification":Qualification[j]}
					doc3=col.find(query3,{"Qualification":1})
					for t in doc3:
						cou=cou+1
					array1.append(cou)	
					j=j+1
					cou=0
				if(k in range(len(AgeGroup))):
					query4={"ageGroup":AgeGroup[k]}
					doc4=col.find(query4,{"ageGroup":1})
					for t in doc4:
						cou=cou+1
					array2.append(cou)
					k=k+1
					cou=0
				if(v in  range(len(Affiliation))):	
					query5={"Affiliation":Affiliation[v]}
					doc5=col.find(query5,{"Affiliation":1})
					for t in doc5:
						cou=cou+1
					array3.append(cou)	
					v=v+1
					cou=0
				if(u in range(len(Gender))):
					query100={"Gender":Gender[u]}
					doc100=col.find(query100,{"Gender":1})
					for t in doc100:
						cou=cou+1
					array4.append(cou)
					u=u+1
					cou=0
			data.append({'x':Countries,'y':array,'type':'bar','name':'No of registered students'}),
			data1.append({'x':Qualification,'y':array1,'type':'bar','name':'Qualifications'}),
			data2.append({'labels':AgeGroup,'values':array2,'type':'pie','name':'Age Group'}),
			data3.append({'labels':Affiliation,'values':array3,'type':'pie','name':'Affiliation'}),
			data4.append({'labels':Gender,'values':array4,'type':'pie','name':'Gender'})
		if((tab=='tab-2-example')and(count==1)):
			while i in range(len(Countries)) or j in range(len(Qualification))or k in range(len(AgeGroup)) or v in range(len(Affiliation))or u in range(len(Gender)):
				if(selector2 in Gender):	
					if(i in range(len(Countries))):
						query6={"$and":[{"Country":Countries[i]},{"Gender":selector2}]}
						doc6=col.find(query6,{"Country":1,"Gender":1})
						for  t in doc6:
							cou=cou+1
						array.append(cou)
						i=i+1
						cou=0
					if(j in range(len(Qualification))):
						query7={"$and":[{"Qualification":Qualification[j]},{"Gender":selector2}]}
						doc7=col.find(query7,{"Qualification":1})
						for t in doc7:
							cou=cou+1
						array1.append(cou)	
						j=j+1
						cou=0
					if(k in range(len(AgeGroup))):
						query8={"$and":[{"ageGroup":AgeGroup[k]},{"Gender":selector2}]}
						doc8=col.find(query8,{"Gender":1,"ageGroup":1})
						for t in doc8:
							cou=cou+1
						array2.append(cou)	
						k=k+1
						cou=0
					if(v in  range(len(Affiliation))):		
						query9={"$and":[{"Affiliation":Affiliation[v]},{"Gender":selector2}]}
						doc9=col.find(query9,{"Gender":1,"Affiliation":1})
						for t in doc9:
							cou=cou+1
						array3.append(cou)	
						v=v+1		
						cou=0
					if(u in range(len(Gender))):
						query24={"Gender":Gender[u]}
						doc24=col.find(query24,{"Gender":1})
						for t in doc24:
							cou=cou+1
						if(Gender[u]==selector2):
							array4.append(cou)
						else:
							array4.append(0)
						u=u+1
						cou=0
				if(selector1 in Qualification):
					if(i in range(len(Countries))):
						query10={"$and":[{"Country":Countries[i]},{"Qualification":selector1}]}
						doc10=col.find(query10,{"Country":1,"Qualification":1})
						for  t in doc10:
							cou=cou+1
						array.append(cou)
						i=i+1
						cou=0
					if(j in range(len(Qualification))):
						query7={"Qualification":Qualification[j]}
						doc7=col.find(query7,{"Qualification":1})
						for t in doc7:
							cou=cou+1
						if(Qualification[j]==selector1):
							array1.append(cou)
						else:
							array1.append(0)	
						j=j+1
						cou=0
					if(k in range(len(AgeGroup))):
						query11={"$and":[{"ageGroup":AgeGroup[k]},{"Qualification":selector1}]}
						doc11=col.find(query11,{"ageGroup":1,"Qualification":1})
						for t in doc11:
							cou=cou+1
						array2.append(cou)	
						k=k+1
						cou=0
					if(v in  range(len(Affiliation))):		
						query12={"$and":[{"Affiliation":Affiliation[v]},{"Qualification":selector1}]}
						doc12=col.find(query12,{"Affiliation":1,"Qualification":1})
						for t in doc12:
							cou=cou+1
						array3.append(cou)	
						v=v+1
						cou=0
					if(u in range(len(Gender))):
						query25={"$and":[{"Gender":Gender[u]},{"Qualification":selector1}]}
						doc25=col.find(query25,{"Gender":1,"Qualification":1})
						for t in doc25:
							cou=cou+1
						array4.append(cou)
						u=u+1
						cou=0
				if(selector3 in Affiliation):
					if(i in range(len(Countries))):
						query13={"$and":[{"Country":Countries[i]},{"Affiliation":selector3}]}
						doc13=col.find(query13,{"Country":1,"Affiliation":1})
						for  t in doc13:
							cou=cou+1
						array.append(cou)
						i=i+1
						cou=0
					if(j in range(len(Qualification))):
						query14={"$and":[{"Qualification":Qualification[j]},{"Affiliation":selector3}]}
						doc14=col.find(query14,{"Qualification":1,"Affiliation":1})
						for t in doc14:
							cou=cou+1
						array1.append(cou)	
						j=j+1
						cou=0
					if(k in range(len(AgeGroup))):
						query15={"$and":[{"ageGroup":AgeGroup[k]},{"Affiliation":selector3}]}
						doc15=col.find(query15,{"Affiliation":1,"ageGroup":1})
						for t in doc15:
							cou=cou+1
						array2.append(cou)
						k=k+1
						cou=0
					if(v in  range(len(Affiliation))):
						query5={"Affiliation":Affiliation[v]}
						doc5=col.find(query5,{"Affiliation":1})
						for t in doc5:
							cou=cou+1
						if(selector3==Affiliation[v]):
							array3.append(cou)	
						else:
							array3.append(0)
						v=v+1
						cou=0	
					if(u in range(len(Gender))):
						query26={"$and":[{"Gender":Gender[u]},{"Affiliation":selector3}]}
						doc26=col.find(query26,{"Gender":1,"Affiliation":1})
						for t in doc26:
							cou=cou+1
						array4.append(cou)
						u=u+1
						cou=0
				if(selector4 in AgeGroup):
					if(i in range(len(Countries))):
						query13={"$and":[{"Country":Countries[i]},{"ageGroup":selector4}]}
						doc13=col.find(query13,{"Country":1,"ageGroup":1})
						for  t in doc13:
							cou=cou+1
						array.append(cou)
						i=i+1
						cou=0
					if(j in range(len(Qualification))):
						query14={"$and":[{"Qualification":Qualification[j]},{"ageGroup":selector4}]}
						doc14=col.find(query14,{"Qualification":1,"ageGroup":1})
						for t in doc14:
							cou=cou+1
						array1.append(cou)	
						j=j+1
						cou=0
					if(k in range(len(AgeGroup))):
						query15={"ageGroup":AgeGroup[k]}
						doc15=col.find(query15,{"ageGroup":1})
						for t in doc15:
							cou=cou+1
						if(selector4==AgeGroup[k]):	
							array2.append(cou)
						else:
							array2.append(0)
						k=k+1		
						cou=0
					if(v in  range(len(Affiliation))):
						query5={"$and":[{"Affiliation":Affiliation[v]},{"ageGroup":selector4}]}
						doc5=col.find(query5,{"Affiliation":1,"ageGroup":1})
						for t in doc5:
							cou=cou+1
						array3.append(cou)	
						v=v+1
						cou=0
					if(u in range(len(Gender))):
						query27={"$and":[{"Gender":Gender[u]},{"ageGroup":selector4}]}
						doc27=col.find(query27,{"Gender":1,"ageGroup":1})
						for t in doc27:
							cou=cou+1
						array4.append(cou)
						u=u+1
						cou=0
			data.append({'x':Countries,'y':array,'type':'bar','name':'No of registered students'}),
			data1.append({'x':Qualification,'y':array1,'type':'bar','name':'Qualifications'}),
			data2.append({'labels':AgeGroup,'values':array2,'type':'pie','name':'Age Group'}),
			data3.append({'labels':Affiliation,'values':array3,'type':'pie','name':'Affiliation'}),
			data4.append({'labels':Gender,'values':array4,'type':'pie','name':'Gender'})	
		if((tab=='tab-2-example')and((count==2)or(count==3))):
			while i in range(len(Countries)) or j in range(len(Qualification))or k in range(len(AgeGroup)) or v in range(len(Affiliation))or u in range(len(Gender)):
				if(i in range(len(Countries))):
					if((selector1 in Qualification) and(selector2 in Gender) and(selector3 not in Affiliation) and(selector4 not in AgeGroup)):
						query16={"$and":[{"Country":Countries[i]},{"$and" : [{"Qualification":selector1},{"Gender":selector2}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector1 not in Qualification)and(selector4 not in AgeGroup)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Gender":selector2},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation)and(selector2 not in Gender)and(selector4 not in AgeGroup)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector4 in AgeGroup)and(selector3 not in Affiliation)and(selector2 not in Gender)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Qualification":selector1},{"ageGroup":selector4}]}]}
					if((selector2 in Gender)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector3 not in Affiliation)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Gender":selector2},{"ageGroup":selector4}]}]}	
					if((selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector2 not in Gender)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Affiliation":selector3},{"ageGroup":selector4}]}]}	
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 in Affiliation)and (selector4 not in AgeGroup)):
						query16={"$and":[{"Country":Countries[i]},{"$and" : [{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation) and(selector4 in AgeGroup)and(selector2 not in Gender)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector2 in Gender) and(selector4 in AgeGroup)and(selector3 not in Affiliation)):
						query16={"$and":[{"Country":Countries[i]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"ageGroup":selector4}]}]}	
					doc16=col.find(query16)
					for  t in doc16:
						cou=cou+1
					array.append(cou)
					i=i+1
					cou=0
				if(j in range(len(Qualification))):
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 not in Affiliation) and(selector4 not in AgeGroup)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"Gender":selector2}]}]}
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector1 not in Qualification)and(selector4 not in AgeGroup)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Gender":selector2},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation)and(selector2 not in Gender)and(selector4 not in AgeGroup)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector4 in AgeGroup)and(selector3 not in Affiliation)and(selector2 not in Gender)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"ageGroup":selector4}]}]}
					if((selector2 in Gender)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector3 not in Affiliation)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Gender":selector2},{"ageGroup":selector4}]}]}	
					if((selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector2 not in Gender)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Affiliation":selector3},{"ageGroup":selector4}]}]}		
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 in Affiliation)and (selector4 not in AgeGroup)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and" : [{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation) and(selector4 in AgeGroup)and(selector2 not in Gender)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector2 in Gender) and(selector4 in AgeGroup)and(selector3 not in Affiliation)):
						query17={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"ageGroup":selector4}]}]}
					doc17=col.find(query17)
					for t in doc17:
						cou=cou+1
					array1.append(cou)	
					j=j+1
					cou=0
				if(k in range(len(AgeGroup))):
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 not in Affiliation)and(selector4 not in AgeGroup)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"Gender":selector2}]}]}
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector1 not in Qualification)and(selector4 not in AgeGroup)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Gender":selector2},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation)and(selector2 not in Gender)and(selector4 not in AgeGroup)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3}]}]}	
					if((selector1 in Qualification)and(selector4 in AgeGroup)and(selector3 not in Affiliation)and(selector2 not in Gender)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"ageGroup":selector4}]}]}
					if((selector2 in Gender)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector3 not in Affiliation)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Gender":selector2},{"ageGroup":selector4}]}]}	
					if((selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector2 not in Gender)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Affiliation":selector3},{"ageGroup":selector4}]}]}	
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 in Affiliation)and (selector4 not in AgeGroup)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and" : [{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation) and(selector4 in AgeGroup)and(selector2 not in Gender)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector2 in Gender) and(selector4 in AgeGroup)and(selector3 not in Affiliation)):
						query18={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"ageGroup":selector4}]}]}	
					doc18=col.find(query18)
					for t in doc18:
						cou=cou+1
					array2.append(cou)	
					k=k+1
					cou=0
				if(v in range(len(Affiliation))):
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 not in Affiliation)and(selector4 not in AgeGroup)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"Gender":selector2}]}]}
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector1 not in Qualification)and(selector4 not in AgeGroup)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Gender":selector2},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation)and(selector2 not in Gender)and(selector4 not in AgeGroup)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector4 in AgeGroup)and(selector3 not in Affiliation)and(selector2 not in Gender)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"ageGroup":selector4}]}]}
					if((selector2 in Gender)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector3 not in Affiliation)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Gender":selector2},{"ageGroup":selector4}]}]}	
					if((selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector2 not in Gender)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Affiliation":selector3},{"ageGroup":selector4}]}]}	
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 in Affiliation)and (selector4 not in AgeGroup)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and" : [{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation) and(selector4 in AgeGroup)and(selector2 not in Gender)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector2 in Gender) and(selector4 in AgeGroup)and(selector3 not in Affiliation)):
						query19={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"ageGroup":selector4}]}]}		
					doc19=col.find(query19)
					for t in doc19:
						cou=cou+1
					array3.append(cou)	
					v=v+1
					cou=0
				if(u in range(len(Gender))):
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 not in Affiliation)and(selector4 not in AgeGroup)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"Gender":selector2}]}]}
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector1 not in Qualification)and(selector4 not in AgeGroup)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Gender":selector2},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation)and(selector2 not in Gender)and(selector4 not in AgeGroup)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3}]}]}
					if((selector1 in Qualification)and(selector4 in AgeGroup)and(selector3 not in Affiliation)and(selector2 not in Gender)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"ageGroup":selector4}]}]}
					if((selector2 in Gender)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector3 not in Affiliation)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Gender":selector2},{"ageGroup":selector4}]}]}	
					if((selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)and(selector2 not in Gender)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Affiliation":selector3},{"ageGroup":selector4}]}]}	
					if((selector1 in Qualification) and(selector2 in Gender)and(selector3 in Affiliation)and (selector4 not in AgeGroup)):
						query29={"$and":[{"Gender":Gender[u]},{"$and" : [{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3}]}]} 
					if((selector2 in Gender) and(selector3 in Affiliation)and(selector4 in AgeGroup)and(selector1 not in Qualification)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector3 in Affiliation) and(selector4 in AgeGroup)and(selector2 not in Gender)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					if((selector1 in Qualification)and(selector2 in Gender) and(selector4 in AgeGroup)and(selector3 not in Affiliation)):
						query29={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"ageGroup":selector4}]}]}		
					doc29=col.find(query29)
					for t in doc29:
						cou=cou+1
					array4.append(cou)	
					u=u+1
					cou=0
			data.append({'x':Countries,'y':array,'type':'bar','name':'No of registered students'}),
			data1.append({'x':Qualification,'y':array1,'type':'bar','name':'Qualifications'}),
			data2.append({'labels':AgeGroup,'values':array2,'type':'pie','name':'Age Group'}),
			data3.append({'labels':Affiliation,'values':array3,'type':'pie','name':'Affiliation'}),
			data4.append({'labels':Gender,'values':array4,'type':'pie','name':'Gender'})			
		if((tab=='tab-2-example')and(count==4)):
			while i in range(len(Countries)) or j in range(len(Qualification))or k in range(len(AgeGroup)) or v in range(len(Affiliation))or u in range(len(Gender)):
				if(i in range(len(Countries))):
					query20={"$and":[{"Country":Countries[i]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					doc20=col.find(query20,{"Qualification":1,"Gender":1,"Affiliation":1,"ageGroup":1})
					for t in doc20:
						cou=cou+1
					array.append(cou)
					i=i+1
					cou=0
				if(j in range(len(Qualification))):
					query21={"$and":[{"Qualification":Qualification[j]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					doc21=col.find(query21,{"Qualification":1,"Gender":1,"Affiliation":1,"ageGroup":1})
					for t in doc21:
						cou=cou+1
					array1.append(cou)    
					j=j+1
					cou=0
				if(k in range(len(AgeGroup))):
					query22={"$and":[{"ageGroup":AgeGroup[k]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					doc22=col.find(query22,{"Qualification":1,"Gender":1,"Affiliation":1})
					for t in doc22:
						cou=cou+1
					array2.append(cou)    
					k=k+1
					cou=0
				if(v in range(len(Affiliation))):
					query23={"$and":[{"Affiliation":Affiliation[v]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					doc23=col.find(query23,{"Qualification":1,"Gender":1,"Affiliation":1})
					for t in doc23:
						cou=cou+1
					array3.append(cou)    
					v=v+1
					cou=0
				if(u in range(len(Gender))):
					query28={"$and":[{"Gender":Gender[u]},{"$and":[{"Qualification":selector1},{"Gender":selector2},{"Affiliation":selector3},{"ageGroup":selector4}]}]}
					doc28=col.find(query28,{"Gender":1,"Qualification":1})
					for t in doc28:
						cou=cou+1
					array4.append(cou)
					u=u+1
					cou=0
			data.append({'x':Countries,'y':array,'type':'bar','name':'No of registered students'}),
			data1.append({'x':Qualification,'y':array1,'type':'bar','name':'Qualifications'}),
			data2.append({'labels':AgeGroup,'values':array2,'type':'pie','name':'Age Group'}),
			data3.append({'labels':Affiliation,'values':array3,'type':'pie','name':'Affiliation'}),
			data4.append({'labels':Gender,'values':array4,'type':'pie','name':'Gender'})					
		return html.Div([
			dcc.Graph(
			id="bar graph-1",
			figure={"data":data,'layout':{'Gender':{"title":"Countries"},'yaxis':{"title":"No of people with different qualifications"}}}
			),
			dcc.Graph(
			style={'width':'48%','height':'50vh','display':'inline-block'},
			id="pie chart1",
			figure={'data':data2,'layout' :{'title':'simple pie chart'}}
			),
			dcc.Graph(
			style={'width': '48%', 'height': '50vh','display':'inline-block'},
			id="bar graph-2",
			figure={"data":data1,'layout':{'Gender':{"title": "Gender"},'yaxis':{"title":"No of people with different qualifications"}}}
			),
			dcc.Graph(
			style={'width':'48%','height':'50vh','display':'inline-block'},
			id="pie chart2",
			figure={'data':data3,'layout' :{'title':'simple pie chart'}}
			),
			dcc.Graph(
			style={'width':'48%','height':'50vh','display':'inline-block'},
			id="pie chart3",
			figure={'data':data4,'layout' :{'title':'simple pie chart'}}
			)
		])
	else:
		return []
if  __name__ =='__main__':
    app.run_server(debug=True)
        