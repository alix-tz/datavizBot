# -*- coding: utf-8 -*-

########################################################
#                       PACKAGES                       #
########################################################
import random
import plotly.plotly as py
import plotly.graph_objs as go
from sample import finalSample as sample
from sample import wordlinks, lightbgcolors
from code import previouscodes
from secrets import plotkey, plotusername

########################################################
#                  AUTHENTIFICATION                    #
########################################################

py.sign_in(plotusername, plotkey)

########################################################
#                      FUNCTIONS                       #
########################################################

def pickColor():
    """
    Creates a string object refering to a hex color chosen randomly among a pre-set list
    :return: string
    """
    color = random.choice(lightbgcolors)
    return color


def createTitle(listname):
    """
    Creates a title for the chart
    :param listname: list
    :return: string
    """
    link = random.choice(wordlinks)
    if len(listname) > 2:
        title = str(listname[0]) + link + '<br>' + str(listname[1]) + ' (and more)'
    else:
        title = str(listname[0]) + link + '<br>' + str(listname[1])
    return title


def createDataBar(xData, yData, name):
    """
    Creates a bar object for bar charts
    :param xData: list
    :param yData: list
    :param name: string
    :param orientation: string
    :return: plotly.graph_objs.graph_objs.Bar
    """
    color1 = pickColor()
    # Creating the bar object to return
    barTrack = go.Bar(
        x=xData,
        y=yData,
        name=name,
        marker=dict(
            color=color1,
            opacity=0.7,
            line=dict(
                color='#FFF',
                width=.5)
        )
        )
    return barTrack


def createDataLine(xData, yData, name, mode, shape):
    """
    Creates a scatter object for line charts
    :param xData: list
    :param yData: list
    :param name: string
    :param mode: string
    :param shape: string
    :return: plotly.graph_objs.graph_objs.Scatter
    """
    color = pickColor()
    # creating the scatter object to return
    lineTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode=mode,
        line=dict(
            color=color,
            shape=shape
        )
    )
    return lineTrack


def createDataFill(xData, yData, name, mode):
    """
    Creates a scatter object for filled-line charts
    :param xData: list
    :param yData: list
    :param name: string
    :param mode: string
    :return: plotly.graph_objs.graph_objs.Scatter
    """
    color = pickColor()
    # creating the scatter object to return
    fillTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        fill='tozeroy',
        mode=mode,
        line=dict(
            color=color
        )
    )
    return fillTrack


def createDataDot(xData, yData, name, symbol):
    """
    Creates a scatter object for dot charts
    :param xData: list
    :param yData: list
    :param name: string
    :param symbol: string
    :return: plotly.graph_objs.graph_objs.Scatter
    """
    color1 = pickColor()
    color2 = pickColor()
    # creating the scatter object to return
    dotTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode='markers',
        marker=dict(
            color=color1,
            line=dict(
                color=color2,
                width=1
            ),
            symbol=symbol
        )
    )
    return dotTrack


def createDataBubble(xData, yData, zData, name):
    """
    Creates a scatter object for bubble charts
    :param xData: list
    :param yData: list
    :param zData: list
    :param name: string
    :return: plotly.graph_objs.graph_objs.Scatter
    """
    color = pickColor()
    # creating the scatter object to return
    bubbleTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode='markers',
        marker=dict(
            color=color,
            line=dict(
                color='#000',
                width=1
            ),
            size=zData
        )
    )
    return bubbleTrack


def retrieveDataTrack(track, scn, mode, dotSymbol, lineShape, lineStyle, fillStyle):
    """
    Calculate data from a sample to create traces for charts
    Call appropriate function depending on the scenario and chart mode indicated
    :param track: integer
    :param scn: string
    :param mode: string
    :param orientation: string
    :param dotSymbol: string
    :param lineShape: string
    :param lineStyle: string
    :param fillStyle: string
    :return: tuple containing plotly.graph_objs.graph_objs.Scatter for data list, then the name of current dataset
    """
    databundle = sample[str(track)]
    xData = databundle['x'][1]
    yData = databundle['y'][1]
    yName = databundle['y'][0][0]
    zData = databundle['z'][1]
    zName = databundle['z'][0][0]
    trackName = databundle['name']
    # Chosing wether the y axis will dwell from yData or zData
    axis = random.choice(['y','z'])
    if axis == 'z':
        rData = zData
        rName = zName
    else:
        rData = yData
        rName = yName

    if scn == 'barscn':
        trackData = createDataBar(xData, rData, rName)
    elif scn == 'scatscn':
        if mode == 'f':
            trackData = createDataFill(xData, rData, rName, fillStyle)
        elif mode == 'b':
            trackData = createDataBubble(xData, yData, zData, trackName)
        elif mode == 'l':
            trackData = createDataLine(xData, rData, rName, lineStyle, lineShape)
        elif mode == 'd':
            trackData = createDataDot(xData, rData, rName, dotSymbol)
    return trackData, trackName


# ------------------------------------------------------#
#                      BAR SCENARIOS                    #
# ------------------------------------------------------#
def groupLayout(title, orientation):
    """
    creates layout object for group style bar layout
    :param title: string
    :return: plotly.graph_objs.graph_objs.Layout
    """
    layout = go.Layout(
        barmode='group',
        orientation=orientation,
        title=title,
        xaxis=dict(tickangle=-45),
        bargap=0.2,
        bargroupgap=0.1,
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    return layout


def stackLayout(title, orientation):
    """
    creates layout object for stack style bar layout
    :param title: string
    :return: plotly.graph_objs.graph_objs.Layout
    """
    layout = go.Layout(
        barmode='stack',
        orientation=orientation,
        title=title,
        xaxis=dict(tickangle=-45),
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    return layout


def barChart(tracks, rMode):
    """
    Triggers bar type chart scenario with appropriate steps to produce a figure
    :param tracks: integer
    :param rMode: string
    :return: plotly.graph_objs.graph_objs.Figure
    """
    data = []
    listname = []
    # Choosing orientation
    rOrientation = random.choice(['h', 'v'])
    # Creating each Bar object, appended to data list object
    for track in tracks:
        trace, tracename = retrieveDataTrack(track, 'barscn', None, None, None, None, None)
        data.append(trace)
        listname.append(tracename)
    # Calculating chart title
    title = createTitle(listname)
    # Creating Layout object
    if rMode == 'g':
        layout = groupLayout(title, rOrientation)
    if rMode == 's':
        layout = stackLayout(title, rOrientation)
    # Generating the figure to return
    fig = go.Figure(data=data, layout=layout)
    return fig


# ------------------------------------------------------#
#                   SCATTER SCENARIOS                   #
# ------------------------------------------------------#

def scatChart(tracks, rMode):
    """
    Triggers scatter type chart scenario with appropriate steps to produce a figure
    :param tracks: integer
    :param rMode: string
    :return: plotly.graph_objs.graph_objs.Figure
    """
    listname = []
    data = []
    # Chosing scatter chart style
    dotSymbol = random.choice(['circle', 'x', 'diamond-wide', 'star-diamond-dot'])
    lineStyle = random.choice(['lines', 'lines+markers'])
    lineShape = random.choice(['hvh', 'spline', 'vhv', 'linear', 'hv'])
    fillStyle = random.choice(['lines', 'none'])
    # Creating each Bar object, appended to data list object
    for track in tracks:
        trace, tracename = retrieveDataTrack(track, 'scatscn', rMode, dotSymbol, lineShape, lineStyle, fillStyle)
        data.append(trace)
        listname.append(tracename)
    # Calculating chart title
    title = createTitle(listname)
    # Creating Layout object
    layout = go.Layout(
        title=title,
        xaxis=dict(
            tickangle=-45,
            showgrid=False,
            showline=True),
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    # Generating the figure to return
    fig = go.Figure(data=data, layout=layout)
    return fig


# ------------------------------------------------------#
#                  HEATMAP SCENARIOS                    #
# ------------------------------------------------------#
def heatmap(track, axis):
    """
    Creates a heatmap style graph and returns it
    :param track: integer
    :param axis: string
    :return: plotly.graph_objs.graph_objs.Figure
    """
    color1 = pickColor()
    color2 = pickColor()
    colorscale = [[0, color1], [1, color2]]
    zData = sample[str(track)][axis][1]
    zName = sample[str(track)][axis][0]
    xData = sample[str(track)]['x'][1]
    title = 'Assessing ' + sample[str(track)]['name'] #-------------------------- MODIFY TITLE CALCULATION
    trace = go.Heatmap(
        z=[zData],
        x=xData,
        y=zName,
        colorscale=colorscale,
        connectgaps=True)
    data = [trace]
    layout = go.Layout(
        title=title,
        xaxis=dict(ticks='', nticks=20),
        yaxis=dict(tickangle=-90)
    )
    fig = go.Figure(data=data, layout=layout)
    return fig


#------------------------------------------------------#
#             TRIGER FIG AND CODE CREATION
#------------------------------------------------------#
def createCode(rKey):
    """
    Trigers the creation of a graph and a unique code for this graph from a random integer
    :param rKey: integer
    :return: tuple containing first plotly.graph_objs.graph_objs.Figure, second string
    """
    trackid =''
    if rKey == 1 or rKey == 2 :
        # Chosing how many tracks will de displayed
        rTracks = random.randint(2,5)
        # Chosing which tracks will be displayed
        tracks = random.sample(range(1, 8), rTracks)
        # Chosing a submode (group or stack) for the bar graph
        rMode = random.choice(['g', 's'])
        # Generating the unique code for the figure
        sTracks = sorted(tracks)
        for x in sTracks:
            trackid = trackid + str(x)
        code = "b" + rMode + str(rTracks) + trackid
        rTrack = None
        axis = None

    elif rKey == 3 or rKey == 4 or rKey == 5:
        # Chosing how many tracks will be displayed
        rTracks = random.randint(2, 5)
        # Chosing which tracks will be displayed
        tracks = random.sample(range(1, 8), rTracks)
        # Chosing a submode (line-filed, line, dot, bubble) for the scatter graph
        rMode = random.choice(['f', 'l', 'd', 'b'])
        # Generating the unique code for the figure
        sTracks = sorted(tracks)
        for x in sTracks:
            trackid = trackid + str(x)
        code = "s" + rMode + str(rTracks) + trackid
        rTrack = None
        axis = None
    elif rKey == 6:
        # Chosing which track will be displayed
        rTrack = random.randint(1,8)
        # Chosing which axis will be displayed
        axis = random.choice(['y','z'])
        # Generating the unique code for the figure
        code = "h" + axis + str(rTrack)
        tracks = None
        rMode = None
    else:
        print("ERROR : unexpected error, random key must be out of range")
    return code, tracks, rMode, rTrack, axis

def checkcodelist(code):
    """
    Verifies if the code generated already exists in the list of previous codes
    :param code: string
    :return: integer
    """
    check = 1
    for x in previouscodes:
        if code == x:
            check = 0
            print("DEBUG : code is " + code + " STARTING OVER")
    return check


def writenewcodelist(code):
    """
    Creates a string containing a list to write into a unique code tracking file
    :param code: string
    :return:
    """
    previous = ""
    for x in previouscodes:
        previous = previous + "'" + x + "',"
    newcodes = "previouscodes=[" + previous + "'" + code + "']"
    with open('code.py', 'w') as file:
        file.write(newcodes)
    return


########################################################
#                        SCRIPT                        #
########################################################
check = 0
code = 0

while check == 0:
    check = checkcodelist(code)
    rKey = random.randint(1, 2)
    print("DEBUG : rKEy = " + str(rKey))
    code, tracks, rMode, rTrack, axis = createCode(rKey)
print("DEBUG : final code is " + code)
# Generating the figure
if rKey == 1 or rKey == 2:
    fig = barChart(tracks, rMode)
elif rKey == 3 or rKey == 4 or rKey == 5:
    fig = scatChart(tracks, rMode)
elif rKey == 6:
    fig = heatmap(rTrack, axis)

writenewcodelist(code)
filename = "images/" + code
py.image.save_as(fig, filename=filename, format='png')