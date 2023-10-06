document.addEventListener("DOMContentLoaded", function(){
    const dateCardsContainer = document.querySelector(".date-cards");
    const prevButton = document.querySelector(".prev-btn");
    const nextButton = document.querySelector(".next-btn");

    const today = new Date();
    const numberOfDaysToShow = 7;

//    function formatDate(date){
//        const options = {month: "short", day: "numeric"};
//        return date.toLocaleDateString(undefined, options);
//    }

    for (let i = 0; i < numberOfDaysToShow; i++){
        const date = new Date(today);
        date.setDate(today.getDate() + i)

        const dateCard = document.createElement("div");
        dateCard.className = "date-card";
        dateCard.textContent = date.toDateString();

        dateCardsContainer.appendChild(dateCard);
    }

    let currentIndex = 0;

    function navigateCards(direction){
        currentIndex += direction;
        if(currentIndex < 0) currentIndex = 0;
        if(currentIndex > numberOfDaysToShow - 5) currentIndex = numberOfDaysToShow - 5;

        dateCardsContainer.style.transform = 'translateX(-${currentIndex * 100}px)';
    }

    prevButton.addEventListener("click", () => navigateCards(-1));
    nextButton.addEventListener("click", () => navigateCards(1));

})