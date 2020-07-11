@file:Suppress("UNCHECKED_CAST")

package com.example.coronawatch

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import com.example.coronawatch.classes.Wilaya
import java.io.*

object ReadWriteFileManager {

    fun writeFile(contect : Context, wilayaList:ArrayList<Wilaya>){



        val fileName = "contact.txt"
        val fos: FileOutputStream = contect.openFileOutput(fileName, AppCompatActivity.MODE_PRIVATE)
        val os = ObjectOutputStream(fos)
        os.writeObject(wilayaList)
        os.close()
        fos.close()


    }



    fun writefileCountries(nContext: Context, countries: ArrayList<Countries>) {

        val fileName = "countries.txt"
        val fos: FileOutputStream = nContext.openFileOutput(fileName, AppCompatActivity.MODE_PRIVATE)
        val os = ObjectOutputStream(fos)
        os.writeObject(countries)
        os.close()
        fos.close()
    }

    fun readFile(contect : Context) : ArrayList<Wilaya>{
        val fileName = "contact.txt"
        try {
            val fis: FileInputStream = contect.openFileInput(fileName)
            var iss = ObjectInputStream(fis)
            val interventions: ArrayList<Wilaya> = iss.readObject() as ArrayList<Wilaya>
            iss.close()
            fis.close()
            return interventions
        }catch (e : FileNotFoundException){
            println("file not found")
        }


        return arrayListOf<Wilaya>()
    }



    fun readCountries(nContext : Context) : ArrayList<Countries>{
        val fileName = "countries.txt"
        try {
            val fis: FileInputStream = nContext.openFileInput(fileName)
            var iss = ObjectInputStream(fis)
            val interventions: ArrayList<Countries> = iss.readObject() as ArrayList<Countries>
            iss.close()
            fis.close()
            return interventions
        }catch (e : FileNotFoundException){
            println("file not found")
        }


        return arrayListOf<Countries>()
    }


    fun writeWilaya(nContext : Context) {
        val listWilaya = arrayListOf<Wilaya>()
        listWilaya.add(
            Wilaya(
                1,
                "أدرار",
                27.875179,
                -0.295720
            )
        )
        listWilaya.add(
            Wilaya(
                2,
                "الشلف",
                36.154816,
                1.325696
            )
        )
        listWilaya.add(
            Wilaya(
                3,
                "الأغواط",
                33.800010,
                2.890250
            )
        )
        listWilaya.add(
            Wilaya(
                4,
                "أم البواقي",
                35.876549,
                7.115390
            )
        )
        listWilaya.add(
            Wilaya(
                5,
                "بااتنة",
                35.3384291,
                5.7315453
            )
        )
        listWilaya.add(
            Wilaya(
                6,
                "بجاية",
                36.7511783,
                5.0643687
            )
        )
        listWilaya.add(
            Wilaya(
                7,
                "بسكرة",
                34.320341,
                4.7246792
            )
        )
        listWilaya.add(
            Wilaya(
                8,
                "بشار",
                31.385726,
                -2.0115958
            )
        )
        listWilaya.add(
            Wilaya(
                9,
                "البليدة",
                36.4701645,
                2.8287985
            )
        )
        listWilaya.add(
            Wilaya(
                10,
                "البويرة",
                36.2316481,
                3.9082579
            )
        )
        listWilaya.add(
            Wilaya(
                11,
                "تمنراست",
                24.3753438,
                4.3208436
            )
        )
        listWilaya.add(
            Wilaya(
                12,
                "تبسة",
                35.124945,
                7.9011735
            )
        )
        listWilaya.add(
            Wilaya(
                13,
                "تلمسان",
                34.881789,
                -1.316699
            )
        )
        listWilaya.add(
            Wilaya(
                14,
                "تيارت",
                34.8947575,
                1.5945792
            )
        )
        listWilaya.add(
            Wilaya(
                15,
                "تيزي وزو",
                36.6816175,
                4.237186
            )
        )
        listWilaya.add(
            Wilaya(
                16,
                "الجزائر",
                36.7753606,
                3.0601882
            )
        )
        listWilaya.add(
            Wilaya(
                17,
                "الجلفة",
                34.342841,
                3.2172531
            )
        )
        listWilaya.add(
            Wilaya(
                18,
                "جيجل",
                36.7292188,
                5.9607776
            )
        )
        listWilaya.add(
            Wilaya(
                19,
                "سطيف",
                36.1892751,
                5.403493
            )
        )
        listWilaya.add(
            Wilaya(
                20,
                "سعيدة",
                34.743349,
                0.2440764
            )
        )
        listWilaya.add(
            Wilaya(
                21,
                "سكيكدة",
                36.7545115,
                6.8856255
            )
        )
        listWilaya.add(
            Wilaya(
                22,
                "سيدي بلعباس",
                34.682268,
                -0.4357555
            )
        )
        listWilaya.add(
            Wilaya(
                23,
                "عنابة",
                36.8982165,
                7.7549272
            )
        )
        listWilaya.add(
            Wilaya(
                24,
                "قالمة",
                36.3491635,
                7.409499
            )
        )
        listWilaya.add(
            Wilaya(
                25,
                "قسنطينة",
                36.364519,
                6.60826
            )
        )
        listWilaya.add(
            Wilaya(
                26,
                "المدية",
                35.9752045,
                3.0123504
            )
        )
        listWilaya.add(
            Wilaya(
                27,
                "مستغانم",
                36.0026915,
                0.3686867
            )
        )
        listWilaya.add(
            Wilaya(
                28,
                "المسيلة",
                35.1300205,
                4.2003107
            )
        )
        listWilaya.add(
            Wilaya(
                29,
                "معسكر",
                35.3978385,
                0.2430195
            )
        )
        listWilaya.add(
            Wilaya(
                30,
                "ورقلة",
                30.9980145,
                6.7664536
            )
        )
        listWilaya.add(
            Wilaya(
                31,
                "وهران",
                35.7032751,
                -0.6492976
            )
        )
        listWilaya.add(
            Wilaya(
                32,
                "البيض",
                32.570303,
                1.1259581
            )
        )
        listWilaya.add(
            Wilaya(
                33,
                "إيليزي",
                27.8528505,
                7.8189636
            )
        )
        listWilaya.add(
            Wilaya(
                34,
                "برج بوعريريج",
                36.095506,
                4.6611002
            )
        )
        listWilaya.add(
            Wilaya(
                35,
                "بومرداس",
                36.7358032,
                3.6163046
            )
        )
        listWilaya.add(
            Wilaya(
                36,
                "الطارف",
                36.6713563,
                8.070134
            )
        )
        listWilaya.add(
            Wilaya(
                37,
                "تيندوف",
                27.543907,
                -6.2400539
            )
        )
        listWilaya.add(
            Wilaya(
                38,
                "تيسيمسيلت",
                35.7858975,
                1.8340957
            )
        )
        listWilaya.add(
            Wilaya(
                39,
                "الوادي",
                33.215441,
                7.1553214
            )
        )
        listWilaya.add(
            Wilaya(
                40,
                "خنشلة",
                34.9133455,
                6.9059431
            )
        )
        listWilaya.add(
            Wilaya(
                41,
                "سوق اهراس",
                36.1378681,
                7.8262426
            )
        )
        listWilaya.add(
            Wilaya(
                42,
                "تيبازة",
                36.5272741,
                2.1683687
            )
        )
        listWilaya.add(
            Wilaya(
                43,
                "ميلة",
                36.2502135,
                6.1652163
            )
        )
        listWilaya.add(
            Wilaya(
                44,
                "عين الدفلر",
                36.1586843,
                2.0842817
            )
        )
        listWilaya.add(
            Wilaya(
                45,
                "النعامة",
                33.2336851,
                -0.8151958
            )
        )
        listWilaya.add(
            Wilaya(
                46,
                "عين تيموشنت",
                35.3650471,
                -0.9452807
            )
        )
        listWilaya.add(
            Wilaya(
                47,
                "غرداية",
                32.440827,
                3.5618209
            )
        )
        listWilaya.add(
            Wilaya(
                48,
                "غيليزان",
                35.8363185,
                0.9118537
            )
        )
        writeFile(nContext , listWilaya)

    }





    fun writeCountries(nContext : Context) {
        val countries = arrayListOf<Countries>()

        countries.add(Countries("AD",42.546245,1.601554,"Andorra"))
        countries.add(Countries("AE",23.424076,53.847818,"United Arab Emirates"))
        countries.add(Countries("AF",33.93911,67.709953,"Afghanistan"))
        countries.add(Countries("AG",17.060816,-61.796428,"Antigua and Barbuda"))
        countries.add(Countries("AI",18.220554,-63.068615,"Anguilla"))
        countries.add(Countries("AL",41.153332,20.168331,"Albania"))
        countries.add(Countries("AM",40.069099,45.038189,"Armenia"))
        countries.add(Countries("AN",12.226079,-69.060087,"Netherlands"))
        countries.add(Countries("AO",-11.202692,17.873887,"Angola"))
        countries.add(Countries("AQ",-75.250973,-0.071389,"Antarctica"))
        countries.add(Countries("AR",-38.416097,-63.616672,"Argentina"))
        countries.add(Countries("AS",-14.270972,-170.132217,"American Samoa"))
        countries.add(Countries("AT",47.516231,14.550072,"Austria"))
        countries.add(Countries("AU",-25.274398,133.775136,"Australia"))
        countries.add(Countries("AW",12.52111,-69.968338,"Aruba"))
        countries.add(Countries("AZ",40.143105,47.576927,"Azerbaijan"))
        countries.add(Countries("BA",43.915886,17.679076,"Bosnia and Herzegovina"))
        countries.add(Countries("BB",13.193887,-59.543198,"Barbados"))
        countries.add(Countries("BD",23.684994,90.356331,"Bangladesh"))
        countries.add(Countries("BE",50.503887,4.469936,"Belgium"))
        countries.add(Countries("BF",12.238333,-1.561593,"Burkina Faso"))
        countries.add(Countries("BG",42.733883,25.48583,"Bulgaria"))
        countries.add(Countries("BH",25.930414,50.637772,"Bahrain"))
        countries.add(Countries("BI",-3.373056,29.918886,"Burundi"))
        countries.add(Countries("BJ",9.30769,2.315834 , "Benin"))
        countries.add(Countries("BM",32.321384,-64.75737,"Bermuda"))
        countries.add(Countries("BO",-16.290154,-63.588653,"Bolivia"))
        countries.add(Countries("BN",4.535277,114.727669,"Brunei"))
        countries.add(Countries("BR",-14.235004,-51.92528,"Brazil"))
        countries.add(Countries("BS",25.03428,-77.39628,"Bahamas"))
        countries.add(Countries("BT",27.514162,90.433601,"Bhutan"))
        countries.add(Countries("BV",-54.423199,3.413194,"Bouvet Island"))
        countries.add(Countries("BW",-22.328474,24.684866,"Botswana"))
        countries.add(Countries("BY",53.709807,27.953389,"Belarus"))
        countries.add(Countries("BZ",17.189877,-88.49765,"Belize"))
        countries.add(Countries("CA",56.130366,-106.346771,"Canada"))
        countries.add(Countries("CC",-12.164165,96.870956,"Cocos [Keeling] Islands"))
        countries.add(Countries("CD",-4.038333,21.758664,"Congo [DRC]"))
        countries.add(Countries("CF",6.611111,20.939444,"Central African Republic"))
        countries.add(Countries("CG",-0.228021,15.827659,"Congo [Republic]"))
        countries.add(Countries("CH",46.818188,8.227512,"Switzerland"))
        countries.add(Countries("CI",7.539989,-5.54708,"Ivory Coast"))
        countries.add(Countries("CK",-21.236736,-159.777671,"Cook Islands"))
        countries.add(Countries("CL",-35.675147,-71.542969,"Chile"))
        countries.add(Countries("CM",7.369722,12.354722,"Cameroon"))
        countries.add(Countries("CN",35.86166,104.195397,"China"))
        countries.add(Countries("CO",4.570868,-74.297333,"Colombia"))
        countries.add(Countries("CR",9.748917,-83.753428,"Costa Rica"))
        countries.add(Countries("CU",21.521757,-77.781167,"Cuba"))
        countries.add(Countries("CV",16.002082,-24.013197,"Cape Verde"))
        countries.add(Countries("CX",-10.447525,105.690449,"Christmas Island"))
        countries.add(Countries("CY",35.126413,33.429859,"Cyprus"))
        countries.add(Countries("CZ",49.817492,15.472962,"Czech Republic"))
        countries.add(Countries("DE",51.165691,10.451526,"Germany"))
        countries.add(Countries("DJ",11.825138,42.590275,"Djibouti"))
        countries.add(Countries("DK",56.26392,9.501785,"Denmark"))
        countries.add(Countries("DM",15.414999,-61.370976,"Dominica"))
        countries.add(Countries("DO",18.735693,-70.162651,"Dominican Republic"))
        countries.add(Countries("DZ",28.033886,1.659626,"Algeria"))
        countries.add(Countries("EC",-1.831239,-78.183406,"Ecuador"))
        countries.add(Countries("EE",58.595272,25.013607,"Estonia"))
        countries.add(Countries("EG",26.820553,30.802498,"Egypt"))
        countries.add(Countries("EH",24.215527,-12.885834,"Western Sahara"))
        countries.add(Countries("ER",15.179384,39.782334,"Eritrea"))
        countries.add(Countries("ES",40.463667,-3.74922,"Spain"))
        countries.add(Countries("ET",9.145,40.489673 , "Ethiopia"))
        countries.add(Countries("FI",61.92411,25.748151,"Finland"))
        countries.add(Countries("FJ",-16.578193,179.414413,"Fiji"))
        countries.add(Countries("FK",-51.796253,-59.523613,"Falkland Islands"))
        countries.add(Countries("FM",7.425554,150.550812,"Micronesia"))
        countries.add(Countries("FO",61.892635,-6.911806,"Faroe Islands"))
        countries.add(Countries("FR",46.227638,2.213749,"France"))
        countries.add(Countries("GA",-0.803689,11.609444,"Gabon"))
        countries.add(Countries("GB",55.378051,-3.435973,"United Kingdom"))
        countries.add(Countries("GD",12.262776,-61.604171,"Grenada"))
        countries.add(Countries("GE",42.315407,43.356892,"Georgia"))
        countries.add(Countries("GF",3.933889,-53.125782,"French Guiana"))
        countries.add(Countries("GG",49.465691,-2.585278,"Guernsey"))
        countries.add(Countries("GH",7.946527,-1.023194,"Ghana"))
        countries.add(Countries("GI",36.137741,-5.345374,"Gibraltar"))
        countries.add(Countries("GL",71.706936,-42.604303,"Greenland"))
        countries.add(Countries("GM",13.443182,-15.310139,"Gambia"))
        countries.add(Countries("GN",9.945587,-9.696645,"Guinea"))
        countries.add(Countries("GP",16.995971,-62.067641,"Guadeloupe"))
        countries.add(Countries("GQ",1.650801,10.267895,"Equatorial Guinea"))
        countries.add(Countries("GR",39.074208,21.824312,"Greece"))
        countries.add(Countries("GS",-54.429579,-36.587909,"South Georgia and the South Sandwich Islands"))
        countries.add(Countries("GT",15.783471,-90.230759,"Guatemala"))
        countries.add(Countries("GU",13.444304,144.793731,"Guam"))
        countries.add(Countries("GW",11.803749,-15.180413,"Guinea-Bissau"))
        countries.add(Countries("GY",4.860416,-58.93018,"Guyana"))
        countries.add(Countries("GZ",31.354676,34.308825,"Gaza Strip"))
        countries.add(Countries("HK",22.396428,114.109497,"Hong Kong"))
        countries.add(Countries("HM",-53.08181,73.504158,"Heard Island and McDonald Islands"))
        countries.add(Countries("HN",15.199999,-86.241905,"Honduras"))
        countries.add(Countries("HR",45.1,15.2,"Croatia"))
        countries.add(Countries("HT",18.971187,-72.285215,"Haiti"))
        countries.add(Countries("HU",47.162494,19.503304,"Hungary"))
        countries.add(Countries("ID",-0.789275,113.921327,"Indonesia"))
        countries.add(Countries("IE",53.41291,-8.24389,"Ireland"))
        countries.add(Countries("IL",31.046051,34.851612,"Israel"))
        countries.add(Countries("IM",54.236107,-4.548056,"Isle of Man"))
        countries.add(Countries("IN",20.593684,78.96288,"India"))
        countries.add(Countries("IO",-6.343194,71.876519,"British Indian Ocean Territory"))
        countries.add(Countries("IQ",33.223191,43.679291,"Iraq"))
        countries.add(Countries("IR",32.427908,53.688046,"Iran"))
        countries.add(Countries("IS",64.963051,-19.020835,"Iceland"))
        countries.add(Countries("IT",41.87194,12.56738,"Italy"))
        countries.add(Countries("JE",49.214439,-2.13125,"Jersey"))
        countries.add(Countries("JM",18.109581,-77.297508,"Jamaica"))
        countries.add(Countries("JO",30.585164,36.238414,"Jordan"))
        countries.add(Countries("JP",36.204824,138.252924,"Japan"))
        countries.add(Countries("KE",-0.023559,37.906193,"Kenya"))
        countries.add(Countries("KG",41.20438,74.766098,"Kyrgyzstan"))
        countries.add(Countries("KH",12.565679,104.990963,"Cambodia"))
        countries.add(Countries("KI",-3.370417,-168.734039,"Kiribati"))
        countries.add(Countries("KM",-11.875001,43.872219,"Comoros"))
        countries.add(Countries("KN",17.357822,-62.782998,"Saint Kitts and Nevis"))
        countries.add(Countries("KP",40.339852,127.510093,"North Korea"))
        countries.add(Countries("KR",35.907757,127.766922,"South Korea"))
        countries.add(Countries("KW",29.31166,47.481766,"Kuwait"))
        countries.add(Countries("KY",19.513469,-80.566956,"Cayman Islands"))
        countries.add(Countries("KZ",48.019573,66.923684,"Kazakhstan"))
        countries.add(Countries("LA",19.85627,102.495496,"Laos"))
        countries.add(Countries("LB",33.854721,35.862285,"Lebanon"))
        countries.add(Countries("LC",13.909444,-60.978893,"Saint Lucia"))
        countries.add(Countries("LI",47.166,9.555373 , "Liechtenstein"))
        countries.add(Countries("LK",7.873054,80.771797,"Sri Lanka"))
        countries.add(Countries("LR",6.428055,-9.429499,"Liberia"))
        countries.add(Countries("LS",-29.609988,28.233608,"Lesotho"))
        countries.add(Countries("LT",55.169438,23.881275,"Lithuania"))
        countries.add(Countries("LU",49.815273,6.129583,"Luxembourg"))
        countries.add(Countries("LV",56.879635,24.603189,"Latvia"))
        countries.add(Countries("LY",26.3351,17.228331 , "Libya"))
        countries.add(Countries("MA",31.791702,-7.09262,"Morocco"))
        countries.add(Countries("MC",43.750298,7.412841,"Monaco"))
        countries.add(Countries("MD",47.411631,28.369885,"Moldova"))
        countries.add(Countries("ME",42.708678,19.37439,"Montenegro"))
        countries.add(Countries("MG",-18.766947,46.869107,"Madagascar"))
        countries.add(Countries("MH",7.131474,171.184478,"Marshall Islands"))
        countries.add(Countries("MK",41.608635,21.745275,"Macedonia [FYROM]"))
        countries.add(Countries("ML",17.570692,-3.996166,"Mali"))
        countries.add(Countries("MM",21.913965,95.956223,"Myanmar [Burma]"))
        countries.add(Countries("MN",46.862496,103.846656,"Mongolia"))
        countries.add(Countries("MO",22.198745,113.543873,"Macau"))
        countries.add(Countries("MP",17.33083,145.38469,"Northern Mariana Islands"))
        countries.add(Countries("MQ",14.641528,-61.024174,"Martinique"))
        countries.add(Countries("MR",21.00789,-10.940835,"Mauritania"))
        countries.add(Countries("MS",16.742498,-62.187366,"Montserrat"))
        countries.add(Countries("MT",35.937496,14.375416,"Malta"))
        countries.add(Countries("MU",-20.348404,57.552152,"Mauritius"))
        countries.add(Countries("MV",3.202778,73.22068,"Maldives"))
        countries.add(Countries("MW",-13.254308,34.301525,"Malawi"))
        countries.add(Countries("MX",23.634501,-102.552784,"Mexico"))
        countries.add(Countries("MY",4.210484,101.975766,"Malaysia"))
        countries.add(Countries("MZ",-18.665695,35.529562,"Mozambique"))
        countries.add(Countries("NA",-22.95764,18.49041,"Namibia"))
        countries.add(Countries("NC",-20.904305,165.618042,"New Caledonia"))
        countries.add(Countries("NE",17.607789,8.081666,"Niger"))
        countries.add(Countries("NF",-29.040835,167.954712,"Norfolk Island"))
        countries.add(Countries("NG",9.081999,8.675277,"Nigeria"))
        countries.add(Countries("NI",12.865416,-85.207229,"Nicaragua"))
        countries.add(Countries("NL",52.132633,5.291266,"Netherlands"))
        countries.add(Countries("NO",60.472024,8.468946,"Norway"))
        countries.add(Countries("NP",28.394857,84.124008,"Nepal"))
        countries.add(Countries("NR",-0.522778,166.931503,"Nauru"))
        countries.add(Countries("NU",-19.054445,-169.867233,"Niue"))
        countries.add(Countries("NZ",-40.900557,174.885971,"New Zealand"))
        countries.add(Countries("OM",21.512583,55.923255,"Oman"))
        countries.add(Countries("PA",8.537981,-80.782127,"Panama"))
        countries.add(Countries("PE",-9.189967,-75.015152,"Peru"))
        countries.add(Countries("PF",-17.679742,-149.406843,"French Polynesia"))
        countries.add(Countries("PG",-6.314993,143.95555,"Papua New Guinea"))
        countries.add(Countries("PH",12.879721,121.774017,"Philippines"))
        countries.add(Countries("PK",30.375321,69.345116,"Pakistan"))
        countries.add(Countries("PL",51.919438,19.145136,"Poland"))
        countries.add(Countries("PM",46.941936,-56.27111,"Saint Pierre and Miquelon"))
        countries.add(Countries("PN",-24.703615,-127.439308,"Pitcairn Islands"))
        countries.add(Countries("PR",18.220833,-66.590149,"Puerto Rico"))
        countries.add(Countries("PS",31.952162,35.233154,"Palestinian Territories"))
        countries.add(Countries("PT",39.399872,-8.224454,"Portugal"))
        countries.add(Countries("PW",7.51498,134.58252 , "Palau"))
        countries.add(Countries("PY",-23.442503,-58.443832,"Paraguay"))
        countries.add(Countries("QA",25.354826,51.183884,"Qatar"))
        countries.add(Countries("RE",-21.115141,55.536384,"RÃ©union"))
        countries.add(Countries("RO",45.943161,24.96676,"Romania"))
        countries.add(Countries("RS",44.016521,21.005859,"Serbia"))
        countries.add(Countries("RU",61.52401,105.318756,"Russia"))
        countries.add(Countries("RW",-1.940278,29.873888,"Rwanda"))
        countries.add(Countries("SA",23.885942,45.079162,"Saudi Arabia"))
        countries.add(Countries("SB",-9.64571,160.156194,"Solomon Islands"))
        countries.add(Countries("SC",-4.679574,55.491977,"Seychelles"))
        countries.add(Countries("SD",12.862807,30.217636,"Sudan"))
        countries.add(Countries("SE",60.128161,18.643501,"Sweden"))
        countries.add(Countries("SG",1.352083,103.819836,"Singapore"))
        countries.add(Countries("SH",-24.143474,-10.030696,"Saint Helena"))
        countries.add(Countries("SI",46.151241,14.995463,"Slovenia"))
        countries.add(Countries("SJ",77.553604,23.670272,"Svalbard and Jan Mayen"))
        countries.add(Countries("SK",48.669026,19.699024,"Slovakia"))
        countries.add(Countries("SL",8.460555,-11.779889,"Sierra Leone"))
        countries.add(Countries("SM",43.94236,12.457777,"San Marino"))
        countries.add(Countries("SN",14.497401,-14.452362,"Senegal"))
        countries.add(Countries("SO",5.152149,46.199616,"Somalia"))
        countries.add(Countries("SR",3.919305,-56.027783,"Suriname"))
        countries.add(Countries("ST",0.18636,6.613081 , "São Tomé and Príncipe"))
        countries.add(Countries("SV",13.794185,-88.89653,"El Salvador"))
        countries.add(Countries("SY",34.802075,38.996815,"Syria"))
        countries.add(Countries("SZ",-26.522503,31.465866,"Swaziland"))
        countries.add(Countries("TC",21.694025,-71.797928,"Turks and Caicos Islands"))
        countries.add(Countries("TD",15.454166,18.732207,"Chad"))
        countries.add(Countries("TF",-49.280366,69.348557,"French Southern Territories"))
        countries.add(Countries("TG",8.619543,0.824782,"Togo"))
        countries.add(Countries("TH",15.870032,100.992541,"Thailand"))
        countries.add(Countries("TJ",38.861034,71.276093,"Tajikistan"))
        countries.add(Countries("TK",-8.967363,-171.855881,"Tokelau"))
        countries.add(Countries("TL",-8.874217,125.727539,"Timor-Leste"))
        countries.add(Countries("TM",38.969719,59.556278,"Turkmenistan"))
        countries.add(Countries("TN",33.886917,9.537499,"Tunisia"))
        countries.add(Countries("TO",-21.178986,-175.198242,"Tonga"))
        countries.add(Countries("TR",38.963745,35.243322,"Turkey"))
        countries.add(Countries("TT",10.691803,-61.222503,"Trinidad and Tobago"))
        countries.add(Countries("TV",-7.109535,177.64933,"Tuvalu"))
        countries.add(Countries("TW",23.69781,120.960515,"Taiwan"))
        countries.add(Countries("TZ",-6.369028,34.888822,"Tanzania"))
        countries.add(Countries("UA",48.379433,31.16558,"Ukraine"))
        countries.add(Countries("UG",1.373333,32.290275,"Uganda"))
        countries.add(Countries("US",37.09024,-95.712891,"US"))
        countries.add(Countries("UY",-32.522779,-55.765835,"Uruguay"))
        countries.add(Countries("UZ",41.377491,64.585262,"Uzbekistan"))
        countries.add(Countries("VA",41.902916,12.453389,"Vatican City"))
        countries.add(Countries("VC",12.984305,-61.287228,"Saint Vincent and the Grenadines"))
        countries.add(Countries("VE",6.42375,-66.58973 , "Venezuela"))
        countries.add(Countries("VG",18.420695,-64.639968,"British Virgin Islands"))
        countries.add(Countries("VI",18.335765,-64.896335,"U.S. Virgin Islands"))
        countries.add(Countries("VN",14.058324,108.277199,"Vietnam"))
        countries.add(Countries("VU",-15.376706,166.959158,"Vanuatu"))
        countries.add(Countries("WF",-13.768752,-177.156097,"Wallis and Futuna"))
        countries.add(Countries("WS",-13.759029,-172.104629,"Samoa"))
        countries.add(Countries("XK",42.602636,20.902977,"Kosovo"))
        countries.add(Countries("YE",15.552727,48.516388,"Yemen"))
        countries.add(Countries("YT",-12.8275,45.166244,"Mayotte"))
        countries.add(Countries("ZA",-30.559482,22.937506,"South Africa"))
        countries.add(Countries("ZM",-13.133897,27.849332,"Zambia"))
        countries.add(Countries("ZW",-19.015438,29.154857,"Zimbabwe"))

        writefileCountries(nContext , countries)
    }

}


class Countries(val id : String , val lat : Double , val lng : Double , val name : String) : Serializable
