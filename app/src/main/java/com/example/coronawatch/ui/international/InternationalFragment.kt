package com.example.coronawatch.ui.international

import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.coronawatch.*
import com.example.coronawatch.api.bitmapDescriptorFromVector
import com.example.coronawatch.api.setMapStyle
import com.example.coronawatch.classes.InfoWilaya
import com.example.coronawatch.ui.download.InternationalViewModel
import com.example.coronawatch.ui.main.MainViewModel
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import com.sothree.slidinguppanel.SlidingUpPanelLayout
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import kotlinx.android.synthetic.main.fragment_international.*
import kotlinx.android.synthetic.main.international_states.*
import java.io.IOException
import java.lang.Exception


class InternationalFragment : Fragment() {

    lateinit var map: SupportMapFragment
    private lateinit var googleMap: GoogleMap
    private lateinit var mainViewModel: MainViewModel
    private var mMap: GoogleMap? = null
    val url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats?country="
    val token = "14ba3d0d9emsh2050ae0635fcdc1p1cc1a2jsne72c2f99765a"
    var infoWilaya = listOf<InfoWilaya>()

    companion object {
        fun newInstance() = InternationalFragment()
    }

    private lateinit var viewModel: InternationalViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        context?.let { ReadWriteFileManager.writeCountries(it) }
        return inflater.inflate(R.layout.fragment_international, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        viewModel = ViewModelProviders.of(this).get(InternationalViewModel::class.java)
        // TODO: Use the ViewModel
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val listCountries = context?.let { ReadWriteFileManager.readCountries(it) }
        val fragmentManager = activity?.supportFragmentManager
        val fragmentTransaction = fragmentManager?.beginTransaction()
        val fragment = SupportMapFragment()

        fragmentTransaction?.replace(R.id.international_map_fragment, fragment)
        fragmentTransaction?.commit()

        fragment.getMapAsync(OnMapReadyCallback { googleMap ->
            googleMap.mapType = GoogleMap.MAP_TYPE_NORMAL
            googleMap.setMaxZoomPreference(5.5F)
            googleMap.setMinZoomPreference(3.0F)
            googleMap.uiSettings.isRotateGesturesEnabled = false
            var location = LatLng(13.03, 77.60)

            context?.let { setMapStyle(googleMap, it) }

            listCountries?.forEach {
                location = LatLng(it.lat, it.lng)
                googleMap.addMarker(
                    MarkerOptions().position(location).title(it.name).icon(
                        context?.let { it1 ->
                            bitmapDescriptorFromVector(
                                it1,
                                R.drawable.ic_fiber_manual_record_black_24dp
                            )
                        }
                    )
                )
            }



            googleMap.setOnMarkerClickListener{
                    marker ->
                international_sliding_layout.panelState = SlidingUpPanelLayout.PanelState.EXPANDED
                country_name.text = "Pays"
                international_cas_confirme.text = "0"
                international_porteurs_virus.text ="0"
                international_nombre_deces.text = "0"

                international_cas_retablis.text = "0"
               val statUrl = url + marker.title.replace(" " , "%")
                println("HHHHHHHHHHHHHHHHH$statUrl")
                val request = Request.Builder().url(statUrl).get().addHeader("x-rapidapi-key", token)
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
                                val buffer = countriesParsing(body.toString() , context)
                                country_name.text = if (buffer.match) marker.title
                                                    else "منطقة غير معرفة"
                                international_cas_confirme.text = buffer.casConfirme.toString()
                                international_porteurs_virus.text =buffer.nbrPorteurVirus.toString()
                                international_nombre_deces.text = buffer.nbrDeces.toString()

                                international_cas_retablis.text = buffer.casRetablis.toString()
                            }
                        }catch (e : Exception){

                        }
                    }
                })

                true
            }

        })



    }

}
