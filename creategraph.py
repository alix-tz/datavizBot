# -*- coding: utf-8 -*-

#------------------------------------------------------------------- ADD OFFLINE SOLLUTION ?

########################################################
#                       PACKAGES                       #
########################################################
import random
import plotly.plotly as py
import plotly.graph_objs as go
from sample import othersample as sample
from code import previouscodes

########################################################
#                      FUNCTIONS                       #
########################################################

def pickColor():
    """
    Creates a string object refering to a hex color chosen randomly among a pre-set list
    :return: string
    """
    color = random.choice(['#003399', '#0033ff', '#006600', '#006699', '#009933','#00cc66', '#00cc33', '#00ff33', '#00ffcc',
                           '#330033', '#3300cc', '#333333', '#3333ff', '#336666', '#660099', '#660000', '#663333', '#666600',
                           '#666600', '#66cc33', '#990033', '#993300', '#990066', '#999933', '#999999', '#99cc00', '#cc0033',
                           '#cc3300', '#cc3333', '#cc3366', '#cc33ff', '#cc9900', '#ccff99', '#ff0033', '#ff3300', '#ff9900',
                           '#ffcc00', '#ffcc33', '#ffff33', '#ff0000', '00ff00', '0000ff'])
    return color


def createTitle(listname):
    """
    Creates a title for the chart
    :param listname: list
    :return: string
    """
    pivot = random.choice([' confrontés aux ', ' en fonction des ', ' comparés aux ', ' au prisme des ', ' croisés avec les', ' à la lumière des ', ' mis en rapport avec les '])
    if len(listname) > 2:
        title = 'Les ' + str(listname[0]) + str(pivot) + str(listname[1]) + ' (et autres données)'
    else:
        title = 'Les ' + str(listname[0]) + str(pivot) + str(listname[1])
    return title


def createDataBar(xData, yData, name, orientation):
    """
    Creates a bar object for bar charts
    :param xData: list
    :param yData: list
    :param name: string
    :param orientation: string
    :return: plotly.graph_objs.graph_objs.Bar
    """
    color1 = pickColor()
    color2 = pickColor()
    # Chosing lining style
    line = random.choice([True, False])
    if line == True:
        marker = dict(color=color1, line=dict(color=color2, width=0.5))
    else:
        marker = dict(color=color1, opacity=1)
    # Creating the bar object to return
    barTrack = go.Bar(
        x=xData,
        y=yData,
        name=name,
        orientation=orientation,
        marker=marker
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
        fill='tonexty',
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


def retrieveDataTrack(track, scn, mode, orientation, dotSymbol, lineShape, lineStyle, fillStyle):
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
        trackData = createDataBar(xData, rData, rName, orientation)
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
def groupLayout(title):
    """
    creates layout object for group style bar layout
    :param title: string
    :return: plotly.graph_objs.graph_objs.Layout
    """
    layout = go.Layout(
        barmode='group',
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


def stackLayout(title):
    """
    creates layout object for stack style bar layout
    :param title: string
    :return: plotly.graph_objs.graph_objs.Layout
    """
    layout = go.Layout(
        barmode='stack',
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
        trace, tracename = retrieveDataTrack(track, 'barscn', None, rOrientation, None, None, None, None)
        data.append(trace)
        listname.append(tracename)
    # Calculating chart title
    title = createTitle(listname)
    # Creating Layout object
    if rMode == 'g':
        layout = groupLayout(title)
    if rMode == 's':
        layout = stackLayout(title)
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
        trace, tracename = retrieveDataTrack(track, 'scatscn', rMode, None, dotSymbol, lineShape, lineStyle, fillStyle)
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
    tData = sample[str(track)][axis][1]
    zData = [tData[:5], tData[5:10], tData[10:]] #----------------- ADAPT TO DATASET LENGTH
    title = sample[str(track)]['name'] #-------------------------- MODIFY TITLE CALCULATION
    trace = go.Heatmap(
        z=zData,
        colorscale=colorscale,
        connectgaps=True)
    data = [trace]
    layout = go.Layout(
        title=title
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
        tracks = random.sample(range(1, 9), rTracks)
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
        tracks = random.sample(range(1, 9), rTracks)
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
        rTrack = random.randint(2,9)
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
    rKey = random.randint(1, 6)
    print("DEBUG : rKEy = " + str(rKey))
    code, tracks, rMode, rTrack, axis = createCode(rKey) 
#    fig, code = createFig(rKey)
# Generating the figure

print("DEBUG : final code is " + code)

if rKey == 1 or rKey == 2:
    fig = barChart(tracks, rMode)
elif rKey == 3 or rKey == 4 or rKey == 5:
    fig = scatChart(tracks, rMode)
elif rKey == 6:
    fig = heatmap(rTrack, axis)

writenewcodelist(code)
filename = "images/" + code
py.image.save_as(fig, filename=filename, format='png')