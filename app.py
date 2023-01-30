# =====================MODULES=====================#
import dash
from dash import dcc, html
from flask import Flask
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.io as pio
from dash.dependencies import Input, Output, State
import json
from dash_bootstrap_templates import load_figure_template

pio.templates.default = "plotly_dark"
load_figure_template(["sketchy", "cyborg", "minty", 'solar', 'darkly'])
# =====================MODULES=====================#
body = {
    'color': '#0ce8b5',
    'text-align': 'center'
}
body_drop = {
    'background-color': '#383535',
    'color': '#0ce8b5',
    'text-align': 'center',
    'height': '40px',
    'width': '700px'
}
body_but = {
    'margin-left': '698px',
    'margin-bottom': '10px',
    'margin-top': '10px',
}
india_states = json.load(open(r"Gathered_data/states_india.geojson", "r"))
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

# =====================APP INITIATION=====================#
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.SOLAR, dbc.icons.BOOTSTRAP])
# =====================APP INITIATION=====================#


# =====================CSV FILES=====================#
# ********************DEFAULT************************#
yearwise_total_suicide = pd.read_csv(r'Gathered_data/Yearwise_Total_Sucide.csv')
Genderwise_total_suicide = pd.read_csv(r'Gathered_data/Genderwise_Total_Sucide.csv')
Gender_total = pd.read_csv(r'Gathered_data/Gender_Total_Sucide.csv')
# ********************DEFAULT************************#

# >>>>>>>>>>>>>>>>>>>>>>>>>2015<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
region_total_eco_2015 = pd.read_csv(r'Gathered_data/economicwise/2015/region_total_kill_2015.csv')
male_female_deathratio_eco_2015 = pd.read_csv(r'Gathered_data/educationwise/2015/MaleFemaleRatioDeath-2015.csv')
# >>>>>>>>>>>>>>>>>>>>>>>>>2015<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2016<<<<<<<<<<<<<<<<<<<<<<<< #
region_total_eco_2016 = pd.read_csv(r'Gathered_data/economicwise/2016/region_total_kill_2016.csv')
male_female_deathratio_eco_2016 = pd.read_csv(r'Gathered_data/professionwise/2016/MaleFemaleRatioDeath-2016.csv')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2016<<<<<<<<<<<<<<<<<<<<<<<< #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2017<<<<<<<<<<<<<<<<<<<<<<<<< #
region_total_eco_2017 = pd.read_csv(r'Gathered_data/economicwise/2017/region_total_kill_2017.csv')
male_female_deathratio_eco_2017 = pd.read_csv(r'Gathered_data/economicwise/2017/MaleFemaleRatioDeath-2017.csv')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2017<<<<<<<<<<<<<<<<<<<<<<<<< #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2018<<<<<<<<<<<<<<<<<<<<<<<<< #
region_total_eco_2018 = pd.read_csv(r'Gathered_data/economicwise/2018/region_total_kill_2018.csv')
male_female_deathratio_eco_2018 = pd.read_csv(r'Gathered_data/economicwise/2018/MaleFemaleRatioDeath-2018.csv')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2018<<<<<<<<<<<<<<<<<<<<<<<<< #

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2019<<<<<<<<<<<<<<<<<<<<<<<<< #
region_total_eco_2019 = pd.read_csv(r'Gathered_data/economicwise/2019/region_total_kill_2019.csv')
male_female_deathratio_eco_2019 = pd.read_csv(r'Gathered_data/economicwise/2019/MaleFemaleRatioDeath-2019.csv')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2019<<<<<<<<<<<<<<<<<<<<<<<<< #

# ********************2015-economic***************#
total_suicide_eco_2015 = pd.read_csv(r'Gathered_data/economicwise/2015/TotalSucide_Economicwise_2015.csv')
male_female_suicide_eco_2015 = pd.read_csv(r'Gathered_data/economicwise/2015/eco_Male_female_sucide_bar_2015.csv')
# ********************2015-economic***************#

# ********************2016-economic***************#
total_suicide_eco_2016 = pd.read_csv(r'Gathered_data/economicwise/2016/TotalSucide_Economicwise_2016.csv')
male_female_suicide_eco_2016 = pd.read_csv(r'Gathered_data/economicwise/2016/eco_Male_female_sucide_bar_2016.csv')
# ********************2016-economic***************#

# ********************2017-economic***************#
total_suicide_eco_2017 = pd.read_csv(r'Gathered_data/economicwise/2017/TotalSucide_Economicwise_2017.csv')
male_female_suicide_eco_2017 = pd.read_csv(r'Gathered_data/economicwise/2017/eco_Male_female_sucide_bar_2017.csv')
# ********************2017-economic***************#

# ********************2018-economic***************#
total_suicide_eco_2018 = pd.read_csv(r'Gathered_data/economicwise/2018/TotalSucide_Economicwise_2018.csv')
male_female_suicide_eco_2018 = pd.read_csv(r'Gathered_data/economicwise/2018/eco_Male_female_sucide_bar_2018.csv')
# ********************2018-economic***************#

# ********************2019-economic***************#
total_suicide_eco_2019 = pd.read_csv(r'Gathered_data/economicwise/2019/TotalSucide_Economicwise_2019.csv')
male_female_suicide_eco_2019 = pd.read_csv(r'Gathered_data/economicwise/2019/eco_Male_female_sucide_bar_2019.csv')
# ********************2019-economic***************#

# ********************2015-education***************#
total_suicide_edu_2015 = pd.read_csv(r'Gathered_data/educationwise/2015/TotalSucide_educationwise_2015.csv')
male_female_suicide_edu_2015 = pd.read_csv(r'Gathered_data/educationwise/2015/edu_Male_female_sucide_bar_2015.csv')
# ********************2015-education***************#

# ********************2016-education***************#
total_suicide_edu_2016 = pd.read_csv(r'Gathered_data/educationwise/2016/TotalSucide_educationwise_2016.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_edu_2016 = pd.read_csv(r'Gathered_data/educationwise/2016/edu_Male_female_sucide_bar_2016.csv',
                                           encoding='latin1', low_memory=False)
# ********************2016-education***************#

# ********************2017-education***************#
total_suicide_edu_2017 = pd.read_csv(r'Gathered_data/educationwise/2017/TotalSucide_educationwise_2017.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_edu_2017 = pd.read_csv(r'Gathered_data/educationwise/2017/edu_Male_female_sucide_bar_2017.csv',
                                           encoding='latin1', low_memory=False)
# ********************2017-education***************#

# ********************2018-education***************#
total_suicide_edu_2018 = pd.read_csv(r'Gathered_data/educationwise/2018/TotalSucide_educationwise_2018.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_edu_2018 = pd.read_csv(r'Gathered_data/educationwise/2018/edu_Male_female_sucide_bar_2018.csv',
                                           encoding='latin1', low_memory=False)
# ********************2018-education***************#

# ********************2019-education***************#
total_suicide_edu_2019 = pd.read_csv(r'Gathered_data/educationwise/2019/TotalSucide_educationwise_2019.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_edu_2019 = pd.read_csv(r'Gathered_data/educationwise/2019/edu_Male_female_sucide_bar_2019.csv',
                                           encoding='latin1', low_memory=False)
# ********************2019-education***************#

# ********************2015-profession***************#
total_suicide_pro_2015 = pd.read_csv(r'Gathered_data/professionwise/2015/TotalSucide_ProfessionWise_2015.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_pro_2015 = pd.read_csv(r'Gathered_data/professionwise/2015/pro_Male_female_sucide_bar_2015.csv',
                                           encoding='latin1', low_memory=False)
# ********************2015-profession***************#

# ********************2016-profession***************#
total_suicide_pro_2016 = pd.read_csv(r'Gathered_data/professionwise/2016/TotalSucide_ProfessionWise_2016.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_pro_2016 = pd.read_csv(r'Gathered_data/professionwise/2016/pro_Male_female_sucide_bar_2016 .csv',
                                           encoding='latin1', low_memory=False)
# ********************2016-profession***************#

# ********************2017-profession***************#
total_suicide_pro_2017 = pd.read_csv(r'Gathered_data/professionwise/2017/TotalSucide_ProfessionWise_2017.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_pro_2017 = pd.read_csv(r'Gathered_data/professionwise/2017/pro_Male_female_sucide_bar_2017 .csv',
                                           encoding='latin1', low_memory=False)
# ********************2017-profession***************#

# ********************2018-profession***************#
total_suicide_pro_2018 = pd.read_csv(r'Gathered_data/professionwise/2018/TotalSucide_ProfessionWise_2018.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_pro_2018 = pd.read_csv(r'Gathered_data/professionwise/2018/pro_Male_female_sucide_bar_2018 .csv',
                                           encoding='latin1', low_memory=False)
# ********************2018-profession***************#

# ********************2019-profession***************#
total_suicide_pro_2019 = pd.read_csv(r'Gathered_data/professionwise/2019/TotalSucide_ProfessionWise_2019.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_pro_2019 = pd.read_csv(r'Gathered_data/professionwise/2019/pro_Male_female_sucide_bar_2019 .csv',
                                           encoding='latin1', low_memory=False)
# ********************2019-profession***************#

# ********************2015-social***************#
total_suicide_sco_2015 = pd.read_csv(r'Gathered_data/socialstatuswise/2015/TotalSucide_SocialstatusWise_2015.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_sco_2015 = pd.read_csv(r'Gathered_data/socialstatuswise/2015/soc_Male_female_sucide_bar_2015.csv',
                                           encoding='latin1', low_memory=False)
# ********************2015-social***************#

# ********************2016-social***************#
total_suicide_sco_2016 = pd.read_csv(r'Gathered_data/socialstatuswise/2016/TotalSucide_SocialstatusWise_2016.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_sco_2016 = pd.read_csv(r'Gathered_data/socialstatuswise/2016/soc_Male_female_sucide_bar_2016.csv',
                                           encoding='latin1', low_memory=False)
# ********************2016-social***************#

# ********************2017-social***************#
total_suicide_sco_2017 = pd.read_csv(r'Gathered_data/socialstatuswise/2017/TotalSucide_SocialstatusWise_2017.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_sco_2017 = pd.read_csv(r'Gathered_data/socialstatuswise/2017/soc_Male_female_sucide_bar_2017.csv',
                                           encoding='latin1', low_memory=False)
# ********************2017-social***************#

# ********************2018-social***************#
total_suicide_sco_2018 = pd.read_csv(r'Gathered_data/socialstatuswise/2018/TotalSucide_SocialstatusWise_2018.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_sco_2018 = pd.read_csv(r'Gathered_data/socialstatuswise/2018/soc_Male_female_sucide_bar_2018.csv',
                                           encoding='latin1', low_memory=False)
# ********************2018-social***************#

# ********************2019-social***************#
total_suicide_sco_2019 = pd.read_csv(r'Gathered_data/socialstatuswise/2019/TotalSucide_SocialstatusWise_2019.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_sco_2019 = pd.read_csv(r'Gathered_data/socialstatuswise/2019/soc_Male_female_sucide_bar_2019.csv',
                                           encoding='latin1', low_memory=False)
# ********************2019-social***************#

# ********************2015-sucideMeans***************#
total_suicide_scu_2015 = pd.read_csv(r'Gathered_data/sucidemeans/2015/TotalSucide_SucideMeans_2015.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_scu_2015 = pd.read_csv(r'Gathered_data/sucidemeans/2015/scu_Male_female_sucide_bar_2015.csv',
                                           encoding='latin1', low_memory=False)
# ********************2015-sucideMeans***************#

# ********************2016-sucideMeans***************#
total_suicide_scu_2016 = pd.read_csv(r'Gathered_data/sucidemeans/2016/TotalSucide_SucideMeans_2016.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_scu_2016 = pd.read_csv(r'Gathered_data/sucidemeans/2016/scu_Male_female_sucide_bar_2016.csv',
                                           encoding='latin1', low_memory=False)
# ********************2016-sucideMeans***************#

# ********************2017-sucideMeans***************#
total_suicide_scu_2017 = pd.read_csv(r'Gathered_data/sucidemeans/2017/TotalSucide_SucideMeans_2017.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_scu_2017 = pd.read_csv(r'Gathered_data/sucidemeans/2017/scu_Male_female_sucide_bar_2017.csv',
                                           encoding='latin1', low_memory=False)
# ********************2017-sucideMeans***************#

# ********************2018-sucideMeans***************#
total_suicide_scu_2018 = pd.read_csv(r'Gathered_data/sucidemeans/2018/TotalSucide_SucideMeans_2018.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_scu_2018 = pd.read_csv(r'Gathered_data/sucidemeans/2018/scu_Male_female_sucide_bar_2018.csv',
                                           encoding='latin1', low_memory=False)
# ********************2018-sucideMeans***************#

# ********************2019-sucideMeans***************#
total_suicide_scu_2019 = pd.read_csv(r'Gathered_data/sucidemeans/2019/TotalSucide_SucideMeans_2019.csv',
                                     encoding='latin1', low_memory=False)
male_female_suicide_scu_2019 = pd.read_csv(r'Gathered_data/sucidemeans/2019/scu_Male_female_sucide_bar_2019.csv',
                                           encoding='latin1', low_memory=False)
# ********************2019-sucideMeans***************#

# =====================CSV FILES=====================#


# =====================HTML COMPONENTS=====================#
header_comp = html.H3("Suicide Analysis Dashboard of India", style=body)
# =====================HTML COMPONENTS=====================#

# =====================GRAPHICAL COMPONENTS=====================#
# *******************************************************************************DEFAULT*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_1 = px.line(yearwise_total_suicide, x='Year', y='Total', line_shape='spline', markers=True, text='Total',
                template='solar')
fig_1.update_layout(
    title={
        'text': "Yearwise Total Number of Suicides",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    },
    autosize=False,
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_1.update_traces(textposition="bottom right")
fig_1.update_traces(line_color='#5064e6')
fig_1.add_shape(  # add a horizontal "target" line
    type="line", line_color="#41f2e6", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=133618.4, y1=133618.4, yref="y"
)
fig_1.add_annotation(  # add a text callout with arrow
    text="5 Year Average Sucide Value=133618.4", x=2016, y=133618.4, arrowhead=1, showarrow=True
)
fig_1.update_annotations(font=dict(color="#c9c7c9"))
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_2 = px.line(Genderwise_total_suicide, x='Year', y='Total_Male', line_shape='spline', markers=True,
                text='Total_Male', template='solar')
fig_2.update_layout(
    title={
        'text': "Yearwise Total Number of Suicides in Male",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=False,
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_2.update_traces(textposition="bottom right")
fig_2.update_traces(line_color='red')
fig_2.add_shape(  # add a horizontal "target" line
    type="line", line_color="#41f2e6", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=91854.2, y1=91854.2, yref="y"
)
fig_2.add_annotation(  # add a text callout with arrow
    text="5 Year Average Suicide for Males Value=91854.2", x=2016, y=91854.2, arrowhead=1, showarrow=True)
fig_2.update_annotations(font=dict(color="#c9c7c9"))
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_3 = px.line(Genderwise_total_suicide, x='Year', y='Total_Female', line_shape='spline', markers=True,
                text='Total_Female', template='solar')
fig_3.update_layout(
    title={
        'text': "Yearwise Total Number of Suicides in Female",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=False,
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_3.update_traces(textposition="bottom right")
fig_3.update_traces(line_color='orange')

fig_3.add_shape(  # add a horizontal "target" line
    type="line", line_color="#41f2e6", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=41764.2, y1=41764.2, yref="y"
)
fig_3.add_annotation(  # add a text callout with arrow
    text="5 Year Average Suicide for Females Value=41764.2", x=2016, y=41754.2, arrowhead=1, showarrow=True,
)
fig_3.update_annotations(font=dict(color="#c9c7c9"))
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_4 = px.pie(Gender_total, names='Gender', values='Total', hole=0.7, color_discrete_sequence=['#5064e6', '#f29741'],
               hover_data=['Total_Number'], template='solar')
fig_4.update_layout(
    title={
        'text': "Comparison of Total Number of Male and Female Suicides in 5 years",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=False,
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************DEFAULT*******************************************

# *******************************************************************************ECO-2015*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_5 = px.choropleth_mapbox(
    region_total_eco_2015,
    locations="id",
    geojson=india_states,
    color="Total",
    hover_name="State",
    hover_data=["Total"],
    title="Total Numbers of Suicide in India For The Year 2015",
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=2.8,
    opacity=0.5,
    color_continuous_scale=px.colors.diverging.Portland,
    template='solar')
fig_5.update_layout(
    title={
        'text': "Total Numbers of Suicides in India For The Year 2015",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_6 = px.bar(total_suicide_eco_2015, template='solar', x='Categories', y='Total Sucides',
               color='Categories')
fig_6.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Economic Groups in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_6.update_traces(showlegend=False)
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_7 = px.bar(male_female_suicide_eco_2015, x='Categories', y='Total Sucides', color='Gender', barmode='group',
               color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_7.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Economic Groups in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_8 = px.pie(male_female_deathratio_eco_2015, names='Gender', values='Total', hole=0.7,
               color_discrete_sequence=['#5064e6', '#f29741'],
               hover_data=['Total_Number'], template='solar')
fig_8.update_layout(
    title={
        'text': "Percentage of Male and Female Suicides in the Year 2015",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white")
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************ECO-2015*******************************************

# *******************************************************************************ECO-2016*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_9 = px.choropleth_mapbox(
    region_total_eco_2016,
    locations="id",
    geojson=india_states,
    color="Total",
    hover_name="State",
    hover_data=["Total"],
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=2.8,
    opacity=0.5,
    color_continuous_scale=px.colors.diverging.Portland,
    template='solar')
fig_9.update_layout(
    title={
        'text': "Total Numbers of Suicides in India For The Year 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_10 = px.bar(total_suicide_eco_2016, template='solar', x='Categories', y='Total Sucides',
                color='Categories')
fig_10.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Economic Groups in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_10.update_traces(showlegend=False)
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_11 = px.bar(male_female_suicide_eco_2016, x='Categories', y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_11.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Economic Groups in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_12 = px.pie(male_female_deathratio_eco_2016, names='Gender', values='Total', hole=0.7,
                color_discrete_sequence=['#5064e6', '#f29741'],
                hover_data=['Total_Number'], template='solar')
fig_12.update_layout(
    title={
        'text': "Percentage of Male and Female Suicides in the Year 2016",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white")
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************ECO-2016*******************************************

# *******************************************************************************ECO-2017*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_13 = px.choropleth_mapbox(
    region_total_eco_2017,
    locations="id",
    geojson=india_states,
    color="Total",
    hover_name="State",
    hover_data=["Total"],
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=2.8,
    opacity=0.5,
    color_continuous_scale=px.colors.diverging.Portland,
    template='solar')
fig_13.update_layout(
    title={
        'text': "Total Numbers of Suicides in India For The Year 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_14 = px.bar(total_suicide_eco_2017, template='solar', x='Categories', y='Total Sucides',
                color='Categories')
fig_14.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Economic Groups in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_14.update_traces(showlegend=False)
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_15 = px.bar(male_female_suicide_eco_2017, x='Categories', y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_15.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Economic Groups in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_16 = px.pie(male_female_deathratio_eco_2017, names='Gender', values='Total', hole=0.7,
                color_discrete_sequence=['#5064e6', '#f29741'],
                hover_data=['Total_Number'], template='solar')
fig_16.update_layout(
    title={
        'text': "Percentage of Male and Female Suicides in the Year 2017",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white")
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************ECO-2017*******************************************

# *******************************************************************************ECO-2018*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_17 = px.choropleth_mapbox(
    region_total_eco_2018,
    locations="id",
    geojson=india_states,
    color="Total",
    hover_name="State",
    hover_data=["Total"],
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=2.8,
    opacity=0.5,
    color_continuous_scale=px.colors.diverging.Portland,
    template='solar')
fig_17.update_layout(
    title={
        'text': "Total Numbers of Suicides in India For The Year 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_18 = px.bar(total_suicide_eco_2018, template='solar', x='Categories', y='Total Sucides',
                color='Categories')
fig_18.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Economic Groups in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_18.update_traces(showlegend=False)
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_19 = px.bar(male_female_suicide_eco_2018, x='Categories', y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_19.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Economic Groups in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_20 = px.pie(male_female_deathratio_eco_2018, names='Gender', values='Total', hole=0.7,
                color_discrete_sequence=['#5064e6', '#f29741'],
                hover_data=['Total_Number'], template='solar')
fig_20.update_layout(
    title={
        'text': "Percentage of Male and Female Suicides in the Year 2018",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white")
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************ECO-2018*******************************************

# *******************************************************************************ECO-2019*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_21 = px.choropleth_mapbox(
    region_total_eco_2019,
    locations="id",
    geojson=india_states,
    color="Total",
    hover_name="State",
    hover_data=["Total"],
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=2.8,
    opacity=0.5,
    color_continuous_scale=px.colors.diverging.Portland,
    template='solar')
fig_21.update_layout(
    title={
        'text': "Total Numbers of Suicides in India For The Year 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_22 = px.bar(total_suicide_eco_2019, template='solar', x='Categories', y='Total Sucides',
                color='Categories')
fig_22.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Economic Groups in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_22.update_traces(showlegend=False)
# ++++++++++++++++++COMP_2+++++++++++++++++ #

# ++++++++++++++++++COMP_3+++++++++++++++++ #
fig_23 = px.bar(male_female_suicide_eco_2019, x='Categories', y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_23.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Economic Groups in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_3+++++++++++++++++ #

# ++++++++++++++++++COMP_4+++++++++++++++++ #
fig_24 = px.pie(male_female_deathratio_eco_2019, names='Gender', values='Total', hole=0.7,
                color_discrete_sequence=['#5064e6', '#f29741'],
                hover_data=['Total_Number'], template='solar')
fig_24.update_layout(
    title={
        'text': "Percentage of Male and Female Suicides in the Year 2019",
        'y': 0.96,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white")
# ++++++++++++++++++COMP_4+++++++++++++++++ #
# *******************************************************************************ECO-2019*******************************************

# *******************************************************************************EDU-2015*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_25 = px.bar(total_suicide_edu_2015.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_25.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Education Groups in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_25.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_26 = px.bar(male_female_suicide_edu_2015.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_26.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Education Groups in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************EDU-2015*******************************************

# *******************************************************************************EDU-2016*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_27 = px.bar(total_suicide_edu_2016.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_27.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Education Groups in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_27.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_28 = px.bar(male_female_suicide_edu_2016.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_28.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Education Groups in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************EDU-2016*******************************************

# *******************************************************************************EDU-2017*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_29 = px.bar(total_suicide_edu_2017.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_29.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Education Groups in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_29.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_30 = px.bar(male_female_suicide_edu_2017.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_30.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Education Groups in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************EDU-2017*******************************************

# *******************************************************************************EDU-2018*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_31 = px.bar(total_suicide_edu_2018.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_31.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Education Groups in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_31.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_32 = px.bar(male_female_suicide_edu_2018.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_32.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Education Groups in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************EDU-2018*******************************************

# *******************************************************************************EDU-2019*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_33 = px.bar(total_suicide_edu_2019.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_33.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Education Groups in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_33.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_34 = px.bar(male_female_suicide_edu_2019.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_34.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Education Groups in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************EDU-2019*******************************************

# *******************************************************************************PRO-2015*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_35 = px.bar(total_suicide_pro_2015.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_35.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Profession in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_35.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_36 = px.bar(male_female_suicide_pro_2015.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_36.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Professions in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************PRO-2015*******************************************

# *******************************************************************************PRO-2016*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_37 = px.bar(total_suicide_pro_2016.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_37.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Profession in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_37.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_38 = px.bar(male_female_suicide_pro_2016.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_38.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Professions in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************PRO-2016*******************************************

# *******************************************************************************PRO-2017*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_39 = px.bar(total_suicide_pro_2017.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_39.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Profession in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_39.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_40 = px.bar(male_female_suicide_pro_2017.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_40.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Professions in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************PRO-2017*******************************************

# *******************************************************************************PRO-2018*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_41 = px.bar(total_suicide_pro_2018.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_41.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Profession in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_41.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_42 = px.bar(male_female_suicide_pro_2018.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_42.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Professions in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************PRO-2018*******************************************

# *******************************************************************************PRO-2019*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_43 = px.bar(total_suicide_pro_2019.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_43.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Profession in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_43.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_44 = px.bar(male_female_suicide_pro_2019.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_44.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Professions in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************PRO-2019*******************************************

# *******************************************************************************SOC-2015*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_45 = px.bar(total_suicide_sco_2015.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_45.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Social Status in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_45.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_46 = px.bar(male_female_suicide_sco_2015.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_46.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Social Status in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SOC-2015*******************************************

# *******************************************************************************SOC-2016*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_47 = px.bar(total_suicide_sco_2016.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_47.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Social Status in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_47.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_48 = px.bar(male_female_suicide_sco_2016.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_48.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Social Status in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SOC-2016*******************************************

# *******************************************************************************SOC-2017*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_49 = px.bar(total_suicide_sco_2017.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_49.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Social Status in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_49.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_50 = px.bar(male_female_suicide_sco_2017.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_50.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Social Status in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SOC-2017*******************************************

# *******************************************************************************SOC-2018*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_51 = px.bar(total_suicide_sco_2018.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_51.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Social Status in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_51.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_52 = px.bar(male_female_suicide_sco_2018.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_52.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Social Status in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SOC-2018*******************************************

# *******************************************************************************SOC-2019*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_53 = px.bar(total_suicide_sco_2019.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_53.update_layout(
    title={
        'text': "Total Number Of Suicides Based On Social Status in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_53.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_54 = px.bar(male_female_suicide_sco_2019.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_54.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Social Status in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SOC-2019*******************************************

# *******************************************************************************SCU-2015*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_55 = px.bar(total_suicide_scu_2015.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_55.update_layout(
    title={
        'text': "Total Number Of Suicides Based Suicide Means in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_55.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_56 = px.bar(male_female_suicide_scu_2015.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_56.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Suicide Means in 2015",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SCU-2015*******************************************

# *******************************************************************************SCU-2016*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_57 = px.bar(total_suicide_scu_2016.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_57.update_layout(
    title={
        'text': "Total Number Of Suicides Based Suicide Means in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_57.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_58 = px.bar(male_female_suicide_scu_2016.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_58.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Suicide Means in 2016",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SCU-2016*******************************************

# *******************************************************************************SCU-2017*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_59 = px.bar(total_suicide_scu_2017.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_59.update_layout(
    title={
        'text': "Total Number Of Suicides Based Suicide Means in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_59.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_60 = px.bar(male_female_suicide_scu_2017.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_60.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Suicide Means in 2017",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SCU-2017*******************************************

# *******************************************************************************SCU-2018*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_61 = px.bar(total_suicide_scu_2018.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_61.update_layout(
    title={
        'text': "Total Number Of Suicides Based Suicide Means in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_61.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_62 = px.bar(male_female_suicide_scu_2018.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_62.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Suicide Means in 2018",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SCU-2018*******************************************

# *******************************************************************************SCU-2019*******************************************
# ++++++++++++++++++COMP_1+++++++++++++++++ #
fig_63 = px.bar(total_suicide_scu_2019.sort_values('Total Sucides', ascending=False), template='solar', x='Categories',
                y='Total Sucides',
                color='Categories')
fig_63.update_layout(
    title={
        'text': "Total Number Of Suicides Based Suicide Means in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
fig_63.update_traces(showlegend=False)
# ++++++++++++++++++COMP_1+++++++++++++++++ #

# ++++++++++++++++++COMP_2+++++++++++++++++ #
fig_64 = px.bar(male_female_suicide_scu_2019.sort_values('Total Sucides', ascending=False), x='Categories',
                y='Total Sucides', color='Gender', barmode='group',
                color_discrete_sequence=['#5064e6', '#f29741'], template='solar')
fig_64.update_layout(
    title={
        'text': "Total Number of Male and Female Suicides Based on Suicide Means in 2019",
        'y': 0.92,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=700,
    height=500,
    title_font_color="white",
    font_color="white",
)
# ++++++++++++++++++COMP_2+++++++++++++++++ #
# *******************************************************************************SCU-2019*******************************************
# =====================GRAPHICAL COMPONENTS=====================#

# =====================APP LAYOUT=====================#
app.layout = html.Div(
    [
        dbc.Row(
            [
                header_comp
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(['All Year'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "all_year"
                                },
                                {
                                    "label": html.Span(['2015'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "2015",
                                },
                                {
                                    "label": html.Span(['2016'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "2016",
                                },
                                {
                                    "label": html.Span(['2017'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "2017",
                                },
                                {
                                    "label": html.Span(['2018'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "2018",
                                },
                                {
                                    "label": html.Span(['2019'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "2019",

                                },
                            ],
                            value='all_year',
                            style=body_drop,
                            clearable=False,
                            id='year-drop'

                        )
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(['All Conditions'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "all_cond"
                                },
                                {
                                    "label": html.Span(['Economic Wise'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "eco",
                                },
                                {
                                    "label": html.Span(['Education Wise'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "edu",
                                },
                                {
                                    "label": html.Span(['Profession Wise'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "pro",
                                },
                                {
                                    "label": html.Span(['Social Status Wise'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "sco",
                                },
                                {
                                    "label": html.Span(['Suicide Methods'],
                                                       style={'color': '#e91e63', 'font-size': 20}),
                                    "value": "scu_me",

                                },
                            ],
                            value='all_cond',
                            style=body_drop,
                            clearable=False,
                            id='category-drop'

                        )
                    ]
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button("Show", outline=True, color="success", className="me-1", id='button-main', value='x')
                    ],
                    style=body_but

                )
            ],

        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='graph-1')
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Graph(id='graph-2')
                    ]
                )],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='graph-3')
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Graph(id='graph-4')
                    ]
                )],
        ),
    ],
)


# =====================APP LAYOUT=====================#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I/O CALLBACKS~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
@app.callback(
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Output('graph-4', 'figure'),
    [Input('button-main', 'n_clicks')],
    [
        State('year-drop', 'value'),
        State('category-drop', 'value')
    ]
)
def DrawGraphs(btn, year, category):
    if btn and year == '2015' and category == 'eco':
        fig5 = fig_5
        fig6 = fig_6
        fig7 = fig_7
        fig8 = fig_8
        return fig5, fig6, fig7, fig8
    elif btn and year == '2016' and category == 'eco':
        fig9 = fig_9
        fig10 = fig_10
        fig11 = fig_11
        fig12 = fig_12
        return fig9, fig10, fig11, fig12
    elif btn and year == '2017' and category == 'eco':
        fig13 = fig_13
        fig14 = fig_14
        fig15 = fig_15
        fig16 = fig_16
        return fig13, fig14, fig15, fig16
    elif btn and year == '2018' and category == 'eco':
        fig17 = fig_17
        fig18 = fig_18
        fig19 = fig_19
        fig20 = fig_20
        return fig17, fig18, fig19, fig20
    elif btn and year == '2019' and category == 'eco':
        fig21 = fig_21
        fig22 = fig_22
        fig23 = fig_23
        fig24 = fig_24
        return fig21, fig22, fig23, fig24
    elif btn and year == '2015' and category == 'edu':
        fig5 = fig_5
        fig25 = fig_25
        fig26 = fig_26
        fig8 = fig_8
        return fig5, fig25, fig26, fig8
    elif btn and year == '2016' and category == 'edu':
        fig9 = fig_9
        fig27 = fig_27
        fig28 = fig_28
        fig12 = fig_12
        return fig9, fig27, fig28, fig12
    elif btn and year == '2017' and category == 'edu':
        fig13 = fig_13
        fig29 = fig_29
        fig30 = fig_30
        fig16 = fig_16
        return fig13, fig29, fig30, fig16
    elif btn and year == '2018' and category == 'edu':
        fig17 = fig_17
        fig31 = fig_31
        fig32 = fig_32
        fig20 = fig_20
        return fig17, fig31, fig32, fig20
    elif btn and year == '2019' and category == 'edu':
        fig21 = fig_21
        fig33 = fig_33
        fig34 = fig_34
        fig24 = fig_24
        return fig21, fig33, fig34, fig24
    elif btn and year == '2015' and category == 'pro':
        fig5 = fig_5
        fig35 = fig_35
        fig36 = fig_36
        fig8 = fig_8
        return fig5, fig35, fig36, fig8
    elif btn and year == '2016' and category == 'pro':
        fig9 = fig_9
        fig37 = fig_37
        fig38 = fig_38
        fig12 = fig_12
        return fig9, fig37, fig38, fig12
    elif btn and year == '2017' and category == 'pro':
        fig13 = fig_13
        fig39 = fig_39
        fig40 = fig_40
        fig16 = fig_16
        return fig13, fig39, fig40, fig16
    elif btn and year == '2018' and category == 'pro':
        fig17 = fig_17
        fig41 = fig_41
        fig42 = fig_42
        fig20 = fig_20
        return fig17, fig41, fig42, fig20
    elif btn and year == '2019' and category == 'pro':
        fig21 = fig_21
        fig43 = fig_43
        fig44 = fig_44
        fig24 = fig_24
        return fig21, fig43, fig44, fig24
    elif btn and year == '2015' and category == 'sco':
        fig5 = fig_5
        fig45 = fig_45
        fig46 = fig_46
        fig8 = fig_8
        return fig5, fig45, fig46, fig8
    elif btn and year == '2016' and category == 'sco':
        fig9 = fig_9
        fig47 = fig_47
        fig48 = fig_48
        fig12 = fig_12
        return fig9, fig47, fig48, fig12
    elif btn and year == '2017' and category == 'sco':
        fig13 = fig_13
        fig49 = fig_49
        fig50 = fig_50
        fig16 = fig_16
        return fig13, fig49, fig50, fig16
    elif btn and year == '2018' and category == 'sco':
        fig17 = fig_17
        fig51 = fig_51
        fig52 = fig_52
        fig20 = fig_20
        return fig17, fig51, fig52, fig20
    elif btn and year == '2019' and category == 'sco':
        fig21 = fig_21
        fig53 = fig_53
        fig54 = fig_54
        fig24 = fig_24
        return fig21, fig53, fig54, fig24
    elif btn and year == '2015' and category == 'scu_me':
        fig5 = fig_5
        fig55 = fig_55
        fig56 = fig_56
        fig8 = fig_8
        return fig5, fig55, fig56, fig8
    elif btn and year == '2016' and category == 'scu_me':
        fig9 = fig_9
        fig57 = fig_57
        fig58 = fig_58
        fig12 = fig_12
        return fig9, fig57, fig58, fig12
    elif btn and year == '2017' and category == 'scu_me':
        fig13 = fig_13
        fig59 = fig_59
        fig60 = fig_60
        fig16 = fig_16
        return fig13, fig59, fig60, fig16
    elif btn and year == '2018' and category == 'scu_me':
        fig17 = fig_17
        fig61 = fig_61
        fig62 = fig_62
        fig20 = fig_20
        return fig17, fig61, fig62, fig20
    elif btn and year == '2019' and category == 'scu_me':
        fig21 = fig_21
        fig63 = fig_63
        fig64 = fig_64
        fig24 = fig_24
        return fig21, fig63, fig64, fig24
    elif year == 'all_year' and category == 'all_cond':
        fig1 = fig_1
        fig2 = fig_2
        fig3 = fig_3
        fig4 = fig_4
        return fig1, fig2, fig3, fig4


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I/O CALLBACKS~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# =====================APP RUNNING=====================#
app.run_server(debug=True)
# =====================APP RUNNING=====================#
