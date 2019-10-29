import matplotlib.pyplot as plt
import numpy as np

# Shapely Library
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString

# SciPy Interpolation https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
from scipy import interpolate

# Track Name from Tracks List
# track_name = "New_York_Track"
# track_name = "Mexico_track"
# track_name = "Canada_Eval"
track_name = "Canada_Training"

# Toronto Turnpike track waypoints
#center_line_waypoints = [[4.609185457229614,1.643046498298645],[4.504319190979004,1.67146497964859],[4.399074554443359,1.6984639763832092],[4.293483018875122,1.724132478237152],[4.187655448913574,1.7487720251083374],[4.081698417663574,1.7727230191230774],[3.97563099861145,1.7962635159492493],[3.869505524635315,1.8197744488716125],[3.763600468635559,1.8441064953804016],[3.6581575870513916,1.8700284957885742],[3.553057551383972,1.8975245356559753],[3.4481170177459717,1.926171064376831],[3.3432644605636597,1.9547145366668701],[3.2383874654769897,1.982143521308899],[3.1319295167922974,2.0092655420303345],[3.02654492855072,2.0406585335731506],[2.9239845275878906,2.07964950799942],[2.8259520530700684,2.12832248210907],[2.732545971870422,2.185194075107575],[2.6429165601730347,2.2447015047073364],[2.5543090105056763,2.3058074712753296],[2.4664459228515625,2.365598440170288],[2.3773385286331177,2.4274550676345825],[2.2884784936904907,2.4898605346679688],[2.197836995124817,2.5495954751968384],[2.102916955947876,2.6027674674987793],[2.002554476261139,2.645362973213196],[1.897580981254578,2.6736689805984497],[1.789713978767395,2.686097025871277],[1.6813725233078003,2.6819549798965454],[1.5749970078468323,2.660743474960327],[1.4726009964942932,2.6243544816970825],[1.3748530149459839,2.5758700370788574],[1.281750500202179,2.518436908721924],[1.1937781870365143,2.453410029411316],[1.1129567921161652,2.3800384998321533],[1.0421969592571259,2.297893524169922],[0.9861142337322235,2.205552577972412],[0.947014570236206,2.104879081249237],[0.9247994124889374,1.9987910389900208],[0.9167823195457458,1.8902974724769592],[0.9209622740745544,1.7814240455627441],[0.936503678560257,1.6736440062522888],[0.9632556438446045,1.568269968032837],[1.0001376271247864,1.465837001800537],[1.0447850227355957,1.3665714859962463],[1.093875676393509,1.2697779536247253],[1.1451406478881836,1.1739444732666016],[1.1981981694698334,1.0790521800518036],[1.253183275461197,0.985353022813797],[1.3102859854698181,0.8929578363895416],[1.3698010444641118,0.8020434081554405],[1.4323539733886719,0.7131966054439545],[1.4986765384674072,0.6271558403968811],[1.569568514823913,0.5448682457208642],[1.6453405022621155,0.4669097065925598],[1.7242580056190497,0.39215361326932846],[1.804488003253936,0.3192039653658873],[1.8858450651168823,0.24728101963410154],[1.9680349230766296,0.17558056116104126],[2.0486620664596558,0.10257739573717117],[2.1293065547943115,0.02980794757604599],[2.2090935111045837,-0.04387355595827103],[2.2870789766311646,-0.11935244500637054],[2.3589104413986206,-0.19992218585684896],[2.416489601135254,-0.29014210030436516],[2.457169532775879,-0.3888736441731453],[2.4800769090652466,-0.49412575364112854],[2.4912240505218506,-0.602191299200058],[2.4985815286636353,-0.710907906293869],[2.509809970855713,-0.8190776705741882],[2.5317574739456177,-0.9251802265644073],[2.5677324533462524,-1.0271103382110596],[2.6162115335464478,-1.1239750683307648],[2.674426555633545,-1.2161155343055725],[2.735548973083496,-1.3058364987373352],[2.7990576028823853,-1.3936030268669128],[2.8660950660705566,-1.4792065024375916],[2.9362080097198486,-1.5624719858169556],[3.008868455886841,-1.6431390047073364],[3.084826946258545,-1.7206114530563354],[3.164761543273926,-1.7943825125694275],[3.2477575540542603,-1.8646840453147888],[3.332667589187622,-1.9321004748344421],[3.4189904928207397,-1.997926950454712],[3.506491541862488,-2.0630074739456177],[3.5949885845184326,-2.1266459822654724],[3.684191584587097,-2.18951553106308],[3.775633454322815,-2.248464524745941],[3.8714624643325806,-2.2978655099868774],[3.972942352294922,-2.3312435150146484],[4.078174591064453,-2.34393048286438],[4.1832311153411865,-2.332993984222412],[4.284292936325073,-2.300551950931549],[4.379820346832275,-2.2515174746513367],[4.47145414352417,-2.193326473236084],[4.56273341178894,-2.1337549686431885],[4.657216787338257,-2.080012023448944],[4.756945610046387,-2.0384190678596497],[4.862459659576418,-2.013380467891693],[4.970647573471069,-2.0032860040664673],[5.0793156623840305,-2.0059640407562256],[5.186042070388794,-2.022897481918335],[5.289485216140747,-2.054390013217926],[5.388495683670044,-2.098896026611328],[5.484181880950926,-2.1510540246963488],[5.57831859588623,-2.2052585482597347],[5.672954559326174,-2.2585664987564096],[5.769561052322388,-2.308664560317993],[5.86968994140625,-2.350277543067932],[5.973845958709717,-2.3786829710006714],[6.080930948257446,-2.39066743850708],[6.1891584396362305,-2.3882399797439575],[6.2973949909210205,-2.376492500305176],[6.405588388442993,-2.362933039665222],[6.514252901077269,-2.3558554649353027],[6.6224071979522705,-2.3618520498275757],[6.72736668586731,-2.385164499282837],[6.8269994258880615,-2.4255974292755127],[6.919412136077883,-2.4812730550766],[7.0064451694488525,-2.5462489128112793],[7.092819452285767,-2.6122244596481323],[7.183058977127073,-2.672051072120665],[7.280209541320801,-2.7190674543380737],[7.3827290534973145,-2.7531665563583374],[7.488784551620483,-2.7765880823135376],[7.596723556518555,-2.7887380123138428],[7.705402851104736,-2.790287494659424],[7.813960552215576,-2.7823420763015747],[7.921756505966188,-2.7679904699325557],[8.02846646308899,-2.746973991394043],[8.133998394012451,-2.7196990251541138],[8.23613452911377,-2.6825735569000244],[8.332922458648682,-2.633623957633972],[8.422791957855225,-2.5729780197143555],[8.505171775817871,-2.504824995994568],[8.580915927886963,-2.4276044368743896],[8.651664733886719,-2.344859480857849],[8.719083309173584,-2.2570735216140756],[8.784222602844238,-2.1693264842033386],[8.844747543334961,-2.079285979270935],[8.89870309829712,-1.9854525327682495],[8.941900730133057,-1.886442482471466],[8.973433494567871,-1.7830125093460083],[8.99543809890747,-1.67678302526474],[9.011030197143555,-1.5691459774971008],[9.019242286682129,-1.460712492465973],[9.020208358764648,-1.3520789742469788],[9.011768817901611,-1.2437620162963867],[8.993597030639648,-1.1366320252418518],[8.963536739349365,-1.0319579541683197],[8.92065954208374,-0.9316902160644531],[8.865981578826904,-0.8372134864330292],[8.798622131347656,-0.7516090571880341],[8.719659805297852,-0.6770026534795761],[8.630758285522461,-0.6159686893224716],[8.532961368560791,-0.5721200853586197],[8.429037094116211,-0.547596201300621],[8.322094917297363,-0.5419068858027458],[8.214502334594727,-0.5509504973888397],[8.107054710388184,-0.5676377415657043],[7.99943470954895,-0.5833219960331917],[7.891502141952515,-0.5876642614603043],[7.784543991088867,-0.5754548460245132],[7.680687427520752,-0.5468097031116486],[7.580629825592041,-0.5049368590116501],[7.485086441040039,-0.4528762549161911],[7.393003940582275,-0.3945930488407612],[7.302894353866577,-0.3335093390196562],[7.215418338775635,-0.2687771514974884],[7.131267786026001,-0.19994257017970085],[7.048273086547852,-0.12489104643464088],[6.968200922012329,-0.053852058947086334],[6.89148736000061,0.024007253348827362],[6.82938289642334,0.10758724808692932],[6.775941610336304,0.199321030639112],[6.737826824188232,0.29889320209622383],[6.709502935409546,0.40252915769815445],[6.681049823760986,0.5060942023992538],[6.644915580749512,0.6065077483654022],[6.594740629196167,0.6999478936195374],[6.529064416885376,0.7834510207176208],[6.450721025466919,0.8565658330917358],[6.365326881408691,0.9224684834480286],[6.278306007385254,0.9864456653594971],[6.18789529800415,1.0452293157577515],[6.092773914337158,1.097053974866867],[5.9950110912323,1.143466979265213],[5.8969035148620605,1.1911115050315857],[5.805736064910889,1.2341663241386414],[5.71117639541626,1.277884155511856],[5.619248390197754,1.3166009783744812],[5.526684045791626,1.3507930040359497],[5.526684045791626,1.3507930040359497],[5.429593563079834,1.3841480016708374],[5.332087993621826,1.416323959827423],[5.230463981628418,1.4498534798622131],[5.127819061279297,1.4835450053215027],[5.025057554244995,1.5168744921684265],[4.921543598175049,1.549900472164154],[4.817766904830933,1.5820860266685486],[4.713661432266235,1.6132075190544128],[4.609185457229614,1.643046498298645]]

# Interpolate racing lane waypoints
# racing_line_waypoints = [
#     [3.02972, 2.39258],
#     [1.37140, 2.19255],
#     [1.02819, 0.811976],
#     [2.17091, -0.407792],
#     [3.34307, -1.66041],
#     [5.00628, -2.29431],
#     [6.87052, -2.74535],
#     [8.63335, -1.91387],
#     [8.43055, -0.556831],
#     [7.82420, -0.282285],
#     [6.77468, 0.192287],
#     [4.49962, 1.66699],
#     #[6.64431, 0.588418],
#     [3.02972, 2.39258]]
#     #[3.09133, 2.31021]]

# points = np.array(racing_line_waypoints)
# x = points[:,0]
# y = points[:,1] 

# tck, u = interpolate.splprep([x, y], s=0)
# unew = np.arange(0, 1.01, 0.01)
# out = interpolate.splev(unew, tck)

# Location of tracks folder
absolute_path = "."

# Get waypoints from numpy file
waypoints = np.load("%s/tracks-npy/%s.npy" % (absolute_path, track_name))
waypoints.shape

# Get number of waypoints
print("Number of waypoints[0] = " + str(waypoints.shape[0]))
print("Number of waypoints[1] = " + str(waypoints.shape[1]))
print("waypoints.shape = " + str(waypoints.shape))

l_center_line = LineString(waypoints[:,0:2])
l_inner_border = LineString(waypoints[:,2:4])
l_outer_border = LineString(waypoints[:,4:6])

# rescale waypoints to centimeter scale
center_line = waypoints[:,0:2] *100
inner_border = waypoints[:,2:4] *100
outer_border = waypoints[:,4:6] *100


# Plot waypoints
for i, point in enumerate(waypoints):
    # print("point.shape = " + str(point.shape))
    waypoint_center_line = (point[0], point[1]) * 10
    waypoint_inner_line = (point[2], point[3]) * 10
    waypoint_outer_line = (point[4], point[5]) * 10
    # plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1])
    # plt.scatter(waypoint_center_line[0], waypoint_center_line[1])
    # plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1])
    plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1], color='green', marker='o', s=1, linewidths=0)
    plt.scatter(waypoint_center_line[0], waypoint_center_line[1], color='red', marker='o', s=8, linewidths=0)
    plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1], color='blue', marker='o', s=1, linewidths=0)
    print("Waypoint " + str(i) + ": " + str(waypoint_center_line))


# plt.plot(x, y, 'x', out[0], out[1])

# for point in center_line_waypoints:
#     plt.scatter(point[0], point[1], c='w', marker='.', s=4, linewidths=0)

track_name = "Canada_Eval"

# Get waypoints from numpy file
waypoints = np.load("%s/tracks-npy/%s.npy" % (absolute_path, track_name))
waypoints.shape

# Get number of waypoints
print("Number of waypoints[0] = " + str(waypoints.shape[0]))
print("Number of waypoints[1] = " + str(waypoints.shape[1]))
print("waypoints.shape = " + str(waypoints.shape))

l_center_line = LineString(waypoints[:,0:2])
l_inner_border = LineString(waypoints[:,2:4])
l_outer_border = LineString(waypoints[:,4:6])

# rescale waypoints to centimeter scale
center_line = waypoints[:,0:2] *100
inner_border = waypoints[:,2:4] *100
outer_border = waypoints[:,4:6] *100


# Plot waypoints
for i, point in enumerate(waypoints):
    # print("point.shape = " + str(point.shape))
    waypoint_center_line = (point[0], point[1]) * 10
    waypoint_inner_line = (point[2], point[3]) * 10
    waypoint_outer_line = (point[4], point[5]) * 10
    # plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1])
    # plt.scatter(waypoint_center_line[0], waypoint_center_line[1])
    # plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1])
    plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1], color='cyan', marker='x', s=1, linewidths=0)
    plt.scatter(waypoint_center_line[0], waypoint_center_line[1], color='purple', marker='x', s=8, linewidths=0)
    plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1], color='black', marker='x', s=1, linewidths=0)
    print("Waypoint " + str(i) + ": " + str(waypoint_center_line))


plt.show()
