const map = L.map('map').setView([20.5937, 78.9629], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

map.on('click', function(e) {
  const marker = L.marker([e.latlng.lat, e.latlng.lng])
    .addTo(map)
    .bindPopup("Saved Location")
    .openPopup();

  fetch("http://localhost:5000/api/places", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      userId: "demoUser",
      name: "Custom Location",
      latitude: e.latlng.lat,
      longitude: e.latlng.lng
    })
  });
});

function searchLocation() {
  const query = document.getElementById("searchBox").value;

  fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${query}`)
    .then(res => res.json())
    .then(data => {
      if (data.length > 0) {
        const lat = data[0].lat;
        const lon = data[0].lon;
        map.setView([lat, lon], 13);
        L.marker([lat, lon]).addTo(map)
          .bindPopup(query)
          .openPopup();
      }
    });
}
