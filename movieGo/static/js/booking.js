let seats = document.querySelector(".all-seats");
for (var i = 0; i < 25; i++) {
    let booked = contentData[i]['is_reserved'] === 1 ? "booked" : "";
    seats.insertAdjacentHTML(
          "beforeend",'<input type="checkbox" name="tickets" id="s' +(i + 2) +'" /><label for="s' +(i + 2) +'" class="seat ' +booked +'"></label>');
}
let tickets = seats.querySelectorAll("input");
tickets.forEach((ticket) => {
        ticket.addEventListener("change", () => {
        let amount = document.querySelector(".amount").innerHTML;
        let count = document.querySelector(".count").innerHTML;
        amount = Number(amount);
        count = Number(count);

         if (ticket.checked) {
            count += 1;
            amount += 200;
         } else {
            count -= 1;
            amount -= 200;
         }
          document.querySelector(".amount").innerHTML = amount;
          document.querySelector(".count").innerHTML = count;
    });
});
document.addEventListener("DOMContentLoaded", function(){
    const dateCardsContainer = document.querySelector(".date-cards");

    var selectedDate = null; // Variable to store the selected date
    var selectedTime = null; // Variable to store the selected time

    function updateURL(datetime) {
        const currentUrl = window.location.href;
        // Extract the query string from the current URL
        const urlParts = currentUrl.split('/show');
        const baseUrl = urlParts[0];

        const url = `${baseUrl}/show?datetime=${datetime}`;
        window.location.href = url;
    }

    for (const date of dates) {
        const dateCard = document.createElement("div");
        dateCard.className = "date-card";
        dateCard.textContent = date['date_time'];

        dateCard.onclick = function () {
            if (i === 0) {
                // If it's the first date card (today), don't update the URL
                return;
            }

            updateURL(date['date_time']); // Call the function to update the URL
        };

        dateCardsContainer.appendChild(dateCard);
    }

    const form = document.querySelector("#seatSelectionForm");
            form.addEventListener("submit", function (e) {
                e.preventDefault(); // Prevent the default form submission behavior

                // Collect selected seat IDs
                const selectedSeatIds = [];
                const checkboxes = document.querySelectorAll("input[type=checkbox]:checked");
                checkboxes.forEach(function (checkbox) {
                    selectedSeatIds.push(checkbox.id);
                });
                console.log(selectedSeatIds)
                // Send the selected seat IDs to the server using an HTTP POST request
                fetch(`/book/movie/${movieId}/show`, {
                    method: "POST",
                    body: JSON.stringify({ selectedSeats: selectedSeatIds, movieShowDate: movieshowdate }),
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
                .then(response => {
                    if(response.redirected){
                        window.location.href = response.url
                    }
                    else{
                        return response.json()
                    }
                })
                .then(data => {
                    console.log(data)
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            });

});

