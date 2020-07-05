package com.example.coronawatch.ui.main

import android.annotation.SuppressLint
import android.content.ContentValues.TAG
import android.content.Context
import android.content.res.Resources
import android.graphics.Bitmap
import android.graphics.Canvas
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders
import com.example.coronawatch.*
import com.example.coronawatch.R
import com.example.coronawatch.api.*
import com.github.mikephil.charting.charts.BarChart
import com.github.mikephil.charting.data.BarData
import com.github.mikephil.charting.data.BarDataSet
import com.github.mikephil.charting.data.BarEntry
import com.google.android.gms.maps.*
import com.google.android.gms.maps.model.*
import com.sothree.slidinguppanel.SlidingUpPanelLayout
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import kotlinx.android.synthetic.main.fragment_main.*
import kotlinx.android.synthetic.main.wilaya_states.*
import retrofit2.*
import java.io.IOException
import java.lang.Exception


@Suppress("CAST_NEVER_SUCCEEDS")
class MainFragment : Fragment() {

    lateinit var map: SupportMapFragment
    private lateinit var googleMap: GoogleMap
    private lateinit var mainViewModel: MainViewModel
    private var mMap: GoogleMap? = null
    var infoWilaya = listOf<InfoWilaya>()
    lateinit var barChart: BarChart
    @SuppressLint("WrongViewCast")
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        mainViewModel =
            ViewModelProviders.of(this).get(MainViewModel::class.java)

        val root = inflater.inflate(R.layout.fragment_main, container, false)

        barChart = root.findViewById(R.id.bar_graph)

        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        context?.let { ReadWriteFileManager.writeWilaya(it) }
        val listWilaya = context?.let { ReadWriteFileManager.readFile(it) }

        val fragmentManager = activity?.supportFragmentManager
        val fragmentTransaction = fragmentManager?.beginTransaction()
        val fragment = SupportMapFragment()

        fragmentTransaction?.replace(R.id.map_fragment, fragment)
        fragmentTransaction?.commit()

        fragment.getMapAsync(OnMapReadyCallback { googleMap ->
            googleMap.mapType = GoogleMap.MAP_TYPE_NORMAL
            googleMap.setMaxZoomPreference(7.5F)
            googleMap.setMinZoomPreference(6.0F)
            googleMap.uiSettings.isRotateGesturesEnabled = false
            var location = LatLng(13.03, 77.60)

            context?.let { setMapStyle(googleMap , it) }

            listWilaya?.forEach {
                location = LatLng(it.latitude, it.longitude)

                googleMap.addMarker(
                    MarkerOptions().position(location).title("${it.id}").icon(
                        context?.let { it1 ->
                            bitmapDescriptorFromVector(
                                it1,
                                R.drawable.ic_fiber_manual_record_black_24dp
                            )
                        }
                    )
                )
            }

            val bounds = LatLngBounds(
                LatLng(22.188810256559687, -4.653530076146126),
                LatLng(36.23320965502827, 8.012905769050121)
            )
            googleMap.setLatLngBoundsForCameraTarget(bounds)

            googleMap.setOnMarkerClickListener{
                /*marker ->
                val regionStats = infoWilaya.filter { it2 -> it2.idRegionSt.toString() == marker.title }
                if (listWilaya != null) {
                    wilaya_name.text = listWilaya[marker.title.toInt()-1].nom
                }
                var casConfirme : Int = 0
                var casSuspects : Int = 0
                var nombreDeces : Int = 0
                var casRetablis : Int = 0
                var porteurs : Int = 0

                    regionStats.forEach {
                        casConfirme +=it.casConfirme
                        casSuspects +=it.nbrGuerisons
                        nombreDeces +=it.nbrDeces
                        casRetablis +=it.casRetablis
                        porteurs +=it.nbrPorteurVirus
                }
                cas_confirme.text = casConfirme.toString()
                porteurs_virus.text = porteurs.toString()
                nombre_deces.text = nombreDeces.toString()
                cas_suspects.text = casSuspects.toString()
                cas_retablis.text = casRetablis.toString()

                sliding_layout.panelState = SlidingUpPanelLayout.PanelState.EXPANDED
                return@setOnMarkerClickListener true*/
                    marker ->
                sliding_layout.panelState = SlidingUpPanelLayout.PanelState.EXPANDED
                wilaya_name.text = "Wilaya"
                cas_confirme.text = "0"
                porteurs_virus.text ="0"
                nombre_deces.text = "0"
                cas_suspects.text ="0"
                cas_retablis.text = "0"
                val url = "$baseUrl/Region/region/${marker.title.toInt()}/statistics/"
                val token = "Token $globalToken"
                val request = Request.Builder().url(url).header("Authorization", token)
                    .build()
                val client = OkHttpClient()
                client.newCall(request).enqueue(object : com.squareup.okhttp.Callback {
                    override fun onFailure(request: Request?, e: IOException?) {

                        print("Failed to execute request")
                    }

                    override fun onResponse(response: com.squareup.okhttp.Response?) {
                        val body = response?.body()?.string()
                        try {
                            activity?.runOnUiThread {

                            val buffer = statsParsing(body.toString() , context)
                                var casConfirme : Int = 0
                                var casSuspects : Int = 0
                                var nombreDeces : Int = 0
                                var casRetablis : Int = 0
                                var porteurs : Int = 0

                                val barEntries = arrayListOf<BarEntry>()
                                val theDates = ArrayList<BarEntry>()
                                var i = 0
                                buffer.forEach {
                                    barEntries.add(BarEntry(it.casConfirme.toFloat() , i.toFloat() , it.dateSt))
                                    //theDates.add(it.dateSt , i.toFloat())
                                    i++
                                    casConfirme +=it.casConfirme
                                    casSuspects +=it.nbrGuerisons
                                    nombreDeces +=it.nbrDeces
                                    casRetablis +=it.casRetablis
                                    porteurs +=it.nbrPorteurVirus

                                }
                                cas_confirme.text = casConfirme.toString()
                                porteurs_virus.text = porteurs.toString()
                                nombre_deces.text = nombreDeces.toString()
                                cas_suspects.text = casSuspects.toString()
                                cas_retablis.text = casRetablis.toString()
                                wilaya_name.text = listWilaya?.get(marker.title.toInt()-1)?.nom
                                val barDataSet = BarDataSet(barEntries , "الحالات المؤكدة")


                                val theData = BarData(BarDataSet(theDates , "Dates"),barDataSet)
                                barChart.data = theData
                                barChart.setTouchEnabled(true)
                                barChart.isDragEnabled = true
                                barChart.setScaleEnabled(true)
                            }
                        }catch (e : Exception){

                        }
                    }
                })



                return@setOnMarkerClickListener true



            }

        })



        //getStats()

    }


    //map Style





    fun getStats() {
        val retrofit = RetrofitClientStats.retrofitInstance
        val service = retrofit.create(Api::class.java)
        val stats_request = service.get_stats_wilaya()

        stats_request.enqueue(object : Callback<Results> {
            override fun onFailure(call: Call<Results>, t: Throwable) {
                Toast.makeText(context, "error getting stats", Toast.LENGTH_SHORT)
                    .show()
            }

            override fun onResponse(
                call: Call<Results>,
                response: Response<Results>
            ) {
                val allStats = response.body()

                if (allStats != null) {
                    println(allStats.resulrs)
                }
                else println("Error getting data ")
            }

        })


    }
}

