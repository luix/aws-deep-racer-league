
import matplotlib.pyplot as plt

params = {
  'all_wheels_on_track': True,
  'x': 4,
  'y': 5,
  'distance_from_center': 0.3,
  'heading': 359.9,
  'progress': 50,
  'steps': 100,
  'speed': 1.0,
  'steering_angle': 6,
  'track_width': 0.2,
  'waypoints': [[ 2.5, 0.75], [3.33, 0.75], [4.17, 0.75], [5.0, 0.75], [5.83, 0.75], [6.67, 0.75], [7.5, 0.75], [8.33, 0.75], [9.17, 0.75], [9.75, 0.94], [10.0, 1.5], [10.0, 1.875], [9.92, 2.125], [9.58, 2.375], [9.17, 2.75], [8.33, 2.5], [7.5, 2.5], [7.08, 2.56], [6.67, 2.625], [5.83, 3.44], [5.0, 4.375], [4.67, 4.69], [4.33, 4.875], [4.0, 5.0], [3.33, 5.0], [2.5, 4.95], [2.08, 4.94], [1.67, 4.875], [1.33, 4.69], [0.92, 4.06], [1.17, 3.185], [1.5, 1.94], [1.6, 1.5], [1.83, 1.125], [2.17, 0.885 ]],
  'closest_waypoints': [3, 4],
  'is_left_of_center': True,
  'is_reversed': True
}

# The Official re:Invent 2019 League Summit Circuit track waypoints
# waypoints = [[ 2.5, 0.75], [3.33, 0.75], [4.17, 0.75], [5.0, 0.75], [5.83, 0.75], [6.67, 0.75], [7.5, 0.75], [8.33, 0.75], [9.17, 0.75], [9.75, 0.94], [10.0, 1.5], [10.0, 1.875], [9.92, 2.125], [9.58, 2.375], [9.17, 2.75], [8.33, 2.5], [7.5, 2.5], [7.08, 2.56], [6.67, 2.625], [5.83, 3.44], [5.0, 4.375], [4.67, 4.69], [4.33, 4.875], [4.0, 5.0], [3.33, 5.0], [2.5, 4.95], [2.08, 4.94], [1.67, 4.875], [1.33, 4.69], [0.92, 4.06], [1.17, 3.185], [1.5, 1.94], [1.6, 1.5], [1.83, 1.125], [2.17, 0.885 ]]

waypoints = [
[
    4.297569990158081,
    0.5397330448031425
],
[
    4.426135540008545,
    0.5324707552790642
],
[
    4.554401397705078,
    0.5215225964784622
],
[
    4.682554960250853,
    0.5093103125691416
],
[
    4.81076455116272,
    0.4975312650203705
],
[
    4.939021587371828,
    0.48632006347179396
],
[
    5.0673229694366455,
    0.4757053032517433
],
[
    5.195682525634766,
    0.4657651409506798
],
[
    5.324104070663452,
    0.45665569603443146
],
[
    5.452584981918337,
    0.44844715669751156
],
[
    5.581110954284666,
    0.44097380340099346
],
[
    5.709682941436768,
    0.43433064222335815
],
[
    5.838313102722167,
    0.42892168462276464
],
[
    5.967003107070923,
    0.42526649311184883
],
[
    6.095737457275391,
    0.42401671037077904
],
[
    6.224462509155273,
    0.4260958954691887
],
[
    6.352993965148928,
    0.43309648707509063
],
[
    6.480926990509033,
    0.44745950773358345
],
[
    6.60721492767334,
    0.4720972925424576
],
[
    6.730256557464598,
    0.5098519548773759
],
[
    6.847713470458984,
    0.562286913394928
],
[
    6.957293510437012,
    0.6297206878662109
],
[
    7.057086944580078,
    0.7109083980321884
],
[
    7.145216941833496,
    0.8045917451381683
],
[
    7.219638109207153,
    0.9095766842365265
],
[
    7.277390003204346,
    1.0244329273700714
],
[
    7.316255331039429,
    1.147063970565796
],
[
    7.336432456970215,
    1.2740939855575537
],
[
    7.3399598598480225,
    1.4027244448661804
],
[
    7.330377578735352,
    1.5310575366020203
],
[
    7.311108827590942,
    1.6583439707756042
],
[
    7.286302089691162,
    1.784678518772127
],
[
    7.262426853179932,
    1.9111739993095398
],
[
    7.2435243129730225,
    2.0385035276412964
],
[
    7.229895830154419,
    2.1665199995040894
],
[
    7.221508026123047,
    2.2949880361557007
],
[
    7.2178895473480225,
    2.423674464225769
],
[
    7.217003107070923,
    2.552411913871767
],
[
    7.217249870300293,
    2.6811360120773315
],
[
    7.2185893058776855,
    2.8099030256271362
],
[
    7.223315000534058,
    2.9385465383529663
],
[
    7.23470401763916,
    3.066743016242981
],
[
    7.2522361278533936,
    3.194298028945923
],
[
    7.274312496185303,
    3.3211315870285034
],
[
    7.299690008163452,
    3.4473434686660767
],
[
    7.324493885040283,
    3.5736535787582397
],
[
    7.342219352722168,
    3.7011890411376953
],
[
    7.3467113971710205,
    3.8296815156936646
],
[
    7.333174467086792,
    3.9576600790023804
],
[
    7.300265073776245,
    4.081979036331177
],
[
    7.248653888702393,
    4.199785470962524
],
[
    7.180784463882446,
    4.309054374694824
],
[
    7.0988969802856445,
    4.408295154571533
],
[
    7.004908561706543,
    4.49617600440979
],
[
    6.9002251625061035,
    4.570901155471802
],
[
    6.786474943161011,
    4.631005525588989
],
[
    6.665883541107178,
    4.675861120223999
],
[
    6.540735483169556,
    4.705899477005005
],
[
    6.41317081451416,
    4.722471475601196
],
[
    6.284543514251709,
    4.727824449539185
],
[
    6.155872106552124,
    4.723554372787476
],
[
    6.028008937835693,
    4.709210634231567
],
[
    5.901467561721802,
    4.685582399368286
],
[
    5.776427507400513,
    4.654885292053223
],
[
    5.652914524078369,
    4.618616342544556
],
[
    5.530797004699707,
    4.577966928482056
],
[
    5.409636497497559,
    4.534324645996094
],
[
    5.2881410121917725,
    4.491730451583862
],
[
    5.164165496826172,
    4.457295656204224
],
[
    5.0374696254730225,
    4.434800624847412
],
[
    4.909079074859619,
    4.425641059875488
],
[
    4.780461072921753,
    4.430031061172485
],
[
    4.653048515319824,
    4.44775915145874
],
[
    4.52802848815918,
    4.478353023529053
],
[
    4.406522035598755,
    4.520907878875732
],
[
    4.28918194770813,
    4.573648929595947
],
[
    4.174270868301392,
    4.631788969039917
],
[
    4.059048056602478,
    4.689186096191406
],
[
    3.9404149055480957,
    4.7390220165252686
],
[
    3.8173729181289673,
    4.776904106140137
],
[
    3.691102981567383,
    4.801426410675049
],
[
    3.563047409057617,
    4.814691066741943
],
[
    3.4344440698623657,
    4.820245027542114
],
[
    3.305700421333313,
    4.821394920349121
],
[
    3.1769593954086304,
    4.820894479751587
],
[
    3.048218011856079,
    4.820664644241333
],
[
    3.048218011856079,
    4.820664644241333
],
[
    2.9194724559783936,
    4.820880174636841
],
[
    2.7907274961471558,
    4.821095705032349
],
[
    2.6619824171066284,
    4.821312189102173
],
[
    2.533239006996155,
    4.821501970291138
],
[
    2.404494524002075,
    4.821454286575317
],
[
    2.275750994682312,
    4.8213136196136475
],
[
    2.1470088958740234,
    4.8214271068573
],
[
    2.01826548576355,
    4.821507453918457
],
[
    1.8895180225372314,
    4.8213489055633545
],
[
    1.7607779502868652,
    4.821394443511963
],
[
    1.6320390105247498,
    4.821597576141357
],
[
    1.503284990787506,
    4.821451425552368
],
[
    1.3745405077934265,
    4.821286916732788
],
[
    1.2458205223083494,
    4.8216423988342285
],
[
    1.117062985897064,
    4.822492837905884
],
[
    0.9882878959178925,
    4.8227880001068115
],
[
    0.8596269190311432,
    4.820428133010864
],
[
    0.7310181558132172,
    4.814824104309082
],
[
    0.6025434136390686,
    4.805191993713379
],
[
    0.47533468902111053,
    4.78622841835022
],
[
    0.3508569002151489,
    4.753763437271118
],
[
    0.23073942959308585,
    4.707441568374634
],
[
    0.11730552092194521,
    4.646768569946289
],
[
    0.013196945190430229,
    4.571254014968872
],
[
    -0.08005090057849884,
    4.4825780391693115
],
[
    -0.16162204742431666,
    4.383089065551758
],
[
    -0.231448695063591,
    4.274989128112793
],
[
    -0.28915811236947775,
    4.15998649597168
],
[
    -0.33395502576604486,
    4.039338111877441
],
[
    -0.36491833999753,
    3.9144675731658936
],
[
    -0.38199926540255547,
    3.786916017532348
],
[
    -0.38788057304918766,
    3.658308982849121
],
[
    -0.38690732792019844,
    3.5294189453125
],
[
    -0.37823414988815784,
    3.400840401649475
],
[
    -0.3620190266519785,
    3.273088574409485
],
[
    -0.33430090080946684,
    3.1475369930267334
],
[
    -0.2914969023549929,
    3.0263675451278687
],
[
    -0.23255691677331924,
    2.9120094776153564
],
[
    -0.1592903845012188,
    2.8058685064315796
],
[
    -0.07487855851650238,
    2.7085275650024414
],
[
    0.019525855779647827,
    2.621039032936096
],
[
    0.12386356480419636,
    2.545973062515259
],
[
    0.23814000189304352,
    2.487069010734558
],
[
    0.3590839952230462,
    2.4431264400482173
],
[
    0.4837196469306946,
    2.410836935043335
],
[
    0.6100225448608398,
    2.38583242893219
],
[
    0.7371078431606293,
    2.3654584884643555
],
[
    0.8644230961799622,
    2.346598505973816
],
[
    0.9909111261367798,
    2.322442412376404
],
[
    1.1145310699939728,
    2.286637544631958
],
[
    1.2321015000343323,
    2.234655499458313
],
[
    1.3405755162239075,
    2.1655415296554565
],
[
    1.4373279809951789,
    2.080714523792266
],
[
    1.5209224820137024,
    1.9829204678535461
],
[
    1.590993046760559,
    1.875100016593933
],
[
    1.648484528064728,
    1.75994449853897
],
[
    1.6945534944534302,
    1.6397045254707336
],
[
    1.7303414344787598,
    1.5161485075950623
],
[
    1.756584048271179,
    1.3901619911193854
],
[
    1.7766339778900146,
    1.2628360390663147
],
[
    1.7997254729270935,
    1.1363070011138916
],
[
    1.8295664787292483,
    1.011215239763259
],
[
    1.8644014596939087,
    0.8869989216327667
],
[
    1.9088225364685059,
    0.7662729620933533
],
[
    1.968119502067566,
    0.6523323506116867
],
[
    2.0408735275268555,
    0.54618139564991
],
[
    2.1250680685043335,
    0.44870425760746
],
[
    2.2196489572525024,
    0.3613910749554634
],
[
    2.3248839378356934,
    0.2879021596163511
],
[
    2.4408570528030396,
    0.2321484126150608
],
[
    2.5639525651931763,
    0.19400515407323837
],
[
    2.690655469894409,
    0.17272009700536728
],
[
    2.8191715478897095,
    0.16816739737987518
],
[
    2.947432041168213,
    0.17985166609287262
],
[
    3.0732250213623047,
    0.20676950737833977
],
[
    3.1954259872436523,
    0.24696138314902782
],
[
    3.3137829303741455,
    0.29761811246862635
],
[
    3.4292285442352295,
    0.35466916114091873
],
[
    3.544338583946228,
    0.4121566154062748
],
[
    3.6628024578094482,
    0.46268341690301895
],
[
    3.7856080532073975,
    0.5009066984057426
],
[
    3.912076473236084,
    0.5244656428694725
],
[
    4.040278911590576,
    0.5369887053966522
],
[
    4.168871641159058,
    0.5416736379265785
],
[
    4.297569990158081,
    0.5397330448031425
]
]

for point in waypoints:
    plt.plot(point[0], point[1], 'k-', lw=0.5, alpha=0.5)
    plt.plot(point[0] + 0.1, point[1] + 0.1, 'k-', lw=0.5, alpha=0.5)
    plt.plot(point[0] - 0.1, point[1] - 0.1, 'k-', lw=0.5, alpha=0.5)
    plt.scatter(point[0], point[1])
    plt.scatter(point[0] + 0.1, point[1] + 0.1)
    plt.scatter(point[0] - 0.1, point[1] - 0.1)

plt.grid(True)
plt.tight_layout()
plt.show()
