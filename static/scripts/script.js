let nav = 0;
let clicked = null;
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

const calendar = document.getElementById('calendar');
const newEventModal = document.getElementById('newEventModal');
const deleteEventModal = document.getElementById('deleteEventModal');
const backDrop = document.getElementById('modalBackDrop');
const eventTitleInput = document.getElementById('eventTitleInput');
const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
//const data_url = {{ url_for("")}}

function openModal(date) {
    clicked = date;

    const eventForDay = events.find(e => e.date === clicked);

    if(eventForDay) {
        document.getElementById('eventText').innerText = eventForDay.title;
        deleteEventModal.style.display = 'block';
    }
    else {
        newEventModal.style.display = 'block';
    }

    backDrop.style.display = 'block';
}

function load() {
    const dt = new Date();

    if (nav !== 0) {
        dt.setMonth(new Date().getMonth() + nav);
    }

    const day = dt.getDate();
    const month = dt.getMonth();
    const year = dt.getFullYear();

    const firstDayOfMonth = new Date(year, month, 1);
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
    });

    const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);

    document.getElementById('monthDisplay').innerText = `${dt.toLocaleDateString('en-us', {month: 'long'})} ${year}`

    calendar.innerHTML = '';
    
    for(let i = 1; i <= paddingDays + daysInMonth; i++) {
        const daySquare = document.createElement('div');
        daySquare.classList.add('day');

        const dayString = `${month + 1}/${i - paddingDays}/${year}`;

        if(i > paddingDays)
        {
            daySquare.innerText = i - paddingDays;

            const eventForDay = events.find(e => e.date === dayString);
            
            if(eventForDay) {
                const eventDiv = document.createElement('div');
                eventDiv.classList.add('event');
                eventDiv.innerText = eventForDay.title;
                daySquare.appendChild(eventDiv);
            }

            daySquare.addEventListener('click', () => openModal(dayString));
        }
        else
        {
            daySquare.classList.add('padding');
        }
        calendar.appendChild(daySquare);
    }
}

function closeModal() {
    eventTitleInput.classList.remove('error');
    newEventModal.style.display = 'none';
    deleteEventModal.style.display = 'none';
    backDrop.style.display = 'none';
    eventTitleInput.value = '';
    clicked = null;
    load();

}

function saveEvent() {
    if(eventTitleInput.value) {
        eventTitleInput.classList.remove('error');

        events.push({
            date: clicked,
            title: eventTitleInput.value,
        });

        // CODE TO UPDATE THE BACKEND
        fetch(`${window.origin}/api/eventData`, {
            method: "POST",
            credentials: "include",
            headers: new Headers({
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify(events)
        })
        .then(function (response){
            
            if(response.status !== 200) {
            console.log(`Response Status was not 200: ${response.status}`);
            return ;
        }
        
            response.json().then(function (data) {
                console.log(data)
            })
        })


        //const formatjson = '{"date": ' + clicked + ', "title": ' + eventTitleInput.value + '}';
        //data.append("date", clicked);
        //data.append("title", eventTitleInput.value);
        //for (const value of data.values()) {
        //    console.log(obj);
        //}
        //console.log(formatjson);
        //console.log(JSON.stringify(events));

        localStorage.setItem('events', JSON.stringify(events));
        closeModal();
    }
    else {
        eventTitleInput.classList.add('error');
    }
}

function deleteEvent() {
    events = events.filter (e => e.date !== clicked);

            // CODE TO UPDATE THE BACKEND
            fetch(`${window.origin}/api/eventData`, {
                method: "POST",
                credentials: "include",
                headers: new Headers({
                    'Content-Type': 'application/json'
                }),
                body: JSON.stringify(events)
            })
            .then(function (response){
                
                if(response.status !== 200) {
                console.log(`Response Status was not 200: ${response.status}`);
                return ;
            }
            
                response.json().then(function (data) {
                    console.log(data)
                })
            })

    localStorage.setItem('events', JSON.stringify(events));
    closeModal();
}

function initButtons() {
    document.getElementById('nextButton').addEventListener('click', () => {
        nav++;
        load();
    });
    document.getElementById('backButton').addEventListener('click',() => {
        nav--;
        load();
    });

    document.getElementById('saveButton').addEventListener('click', saveEvent);
    document.getElementById('cancelButton').addEventListener('click', closeModal);
    document.getElementById('deleteButton').addEventListener('click', deleteEvent);
    document.getElementById('closeButton').addEventListener('click', closeModal);
}
initButtons();
load();