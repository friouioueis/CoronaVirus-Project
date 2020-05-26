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
import com.example.coronawatch.InfoWilaya
import com.example.coronawatch.api.DataService
import com.example.coronawatch.R
import com.example.coronawatch.ReadWriteFileManager
import com.example.coronawatch.api.RetrofitClientInstance
import com.google.android.gms.maps.*
import com.google.android.gms.maps.model.*
import com.sothree.slidinguppanel.SlidingUpPanelLayout
import kotlinx.android.synthetic.main.fragment_main.*
import kotlinx.android.synthetic.main.wilaya_states.*
import retrofit2.*


@Suppress("CAST_NEVER_SUCCEEDS")
class MainFragment : Fragment() {

    lateinit var map: SupportMapFragment
    private lateinit var googleMap: GoogleMap
    private lateinit var mainViewModel: MainViewModel
    private var mMap: GoogleMap? = null
    var infoWilaya = listOf<InfoWilaya>()

    @SuppressLint("WrongViewCast")
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        mainViewModel =
            ViewModelProviders.of(this).get(MainViewModel::class.java)



        return inflater.inflate(R.layout.fragment_main, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
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

            setMapStyle(googleMap)

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
                marker ->
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
                return@setOnMarkerClickListener true
            }

        })

        getStats()

    }


    //map Style
    private fun setMapStyle(map: GoogleMap) {
        try {
            // Customize the styling of the base map using a JSON object defined
            // in a raw resource file.
            val success = map.setMapStyle(
                MapStyleOptions.loadRawResourceStyle(
                    context,
                    R.raw.map_style
                )
            )

            if (!success) {
                Log.e(TAG, "Style parsing failed.")
            }
        } catch (e: Resources.NotFoundException) {
            Log.e(TAG, "Can't find style. Error: ", e)
        }
    }



    private fun bitmapDescriptorFromVector(
        context: Context,
        vectorResId: Int
    ): BitmapDescriptor? {
        val vectorDrawable = ContextCompat.getDrawable(context, vectorResId)
        vectorDrawable!!.setBounds(
            0,
            0,
            vectorDrawable.intrinsicWidth,
            vectorDrawable.intrinsicHeight
        )
        val bitmap = Bitmap.createBitmap(
            vectorDrawable.intrinsicWidth,
            vectorDrawable.intrinsicHeight,
            Bitmap.Config.ARGB_8888
        )
        val canvas = Canvas(bitmap)
        vectorDrawable.draw(canvas)
        return BitmapDescriptorFactory.fromBitmap(bitmap)
    }

    fun getStats() {
        val retrofit = RetrofitClientInstance.retrofitInstance
        val service = retrofit.create(DataService::class.java)
        val stats_request = service.get_stats_wilaya()

        stats_request.enqueue(object : Callback<List<InfoWilaya>> {
            override fun onFailure(call: Call<List<InfoWilaya>>, t: Throwable) {
                Toast.makeText(context, "error getting stats", Toast.LENGTH_SHORT)
                    .show()
            }

            override fun onResponse(
                call: Call<List<InfoWilaya>>,
                response: Response<List<InfoWilaya>>
            ) {
                val allStats = response.body()
                if (allStats != null) {
                    infoWilaya = allStats

                }
                else println("Eroor getting data ")
            }

        })


    }
}
