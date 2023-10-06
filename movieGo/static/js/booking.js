document.addEventListener("DOMContentLoaded", function(){
    const dateCardsContainer = document.querySelector(".date-cards");
    const prevButton = document.querySelector(".prev-btn");
    const nextButton = document.querySelector(".next-btn");

    const today = new Date();
    const numberOfDaysToShow = 7;

    for (let i = 0; i < numberOfDaysToShow; i++){
        const date = new Date(today);
        date.setDate(today.getDate() + i)

        const dateCard = document.createElement("div");
        dateCard.className = "date-card";
        dateCard.textContent = date.toDateString();

        dateCardsContainer.appendChild(dateCard);
    }



})