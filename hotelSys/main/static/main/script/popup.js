function fadeIn(frame){
    document.body.appendChild(frame);
    frame.style.opacity = 0.0;
    let interval = setInterval(()=>{
        if(Number(frame.style.opacity) < 1.0){
            frame.style.opacity = Number(frame.style.opacity)+0.1;
        }    
        else
            clearInterval(interval);
    }, 30)
}

function fadeOut(frame){
    frame.style.opacity = 1.0;
    let interval = setInterval(()=>{
        if(Number(frame.style.opacity) > 0)
            frame.style.opacity = Number(frame.style.opacity)-0.1;
        else{
            clearInterval(interval);
            frame.remove();
        }
    }, 30)
}

function viewRoom(no, capacity, isIdle, ecoclass){
    let frame = document.createElement("div");
    frame.id = "background";

    if(ecoclass == 0)
        ecoclass = "کلاس A";
    else if(ecoclass == 1)
        ecoclass = "کلاس B";
    else if(ecoclass == 2)
        ecoclass = "کلاس C";
    else
        ecoclass = "--"

    frame.innerHTML = `
        <div id="popupframe">
        <div id="closeBox">
            <button id="closeBtn">X</button>
        </div>
        <div id="container">
            <div class="item">
                <span class="label">شماره اتاق:</span>
                <span class="info">${no}</span>
            </div>
            <div class="item">
                <span class="label">ظرفیت اتاق:</span>
                <span class="info">${capacity} نفر</span>
            </div>
            <div class="item">
                <span class="label">وضعیت اتاق:</span>
                <span class="info">${isIdle? "خالی":"اشغال"}</span>
            </div>
            <div class="item">
                <span class="label">کلاس اقتصادی:</span>
                <span class="info">${ecoclass}</span>
            </div>
        </div>
        </div>
    `;

    fadeIn(frame);
    document.getElementById("closeBtn").addEventListener("click", ()=> fadeOut(frame));
    frame.addEventListener("click", () => fadeOut(frame));
}

function viewCustomer(name, family, nationalId, email){
    let frame = document.createElement("div");
    frame.id = "background";

    frame.innerHTML = `
        <div id="popupframe">
        <div id="closeBox">
            <button id="closeBtn">X</button>
        </div>
        <div id="container">
            <div class="item">
                <span class="label">نام و نام خانوادگی:</span>
                <span class="info">${name} ${family}</span>
            </div>
            <div class="item">
                <span class="label">ظرفیت اتاق:</span>
                <span class="info">${nationalId}</span>
            </div>
            <div class="item">
                <span class="label">پست الکترونیکی:</span>
                <span class="info">${email}</span>
            </div>
        </div>
        </div>
    `;

    fadeIn(frame);
    document.getElementById("closeBtn").addEventListener("click", ()=> fadeOut(frame));
    frame.addEventListener("click", () => fadeOut(frame));
}

function rateReserve(username, password, id){
    let frame = document.createElement("div");
    frame.id = "background";

    frame.innerHTML = `
        <div id="popupframe">
            <div id="closeBox">
                <button id="closeBtn">X</button>
            </div>
            <div id="container">
                <form action="http://localhost:8080/main/customer/reservations/${username}/${password}/${id}" method="post">
                    <div id="item">
                        <label for="1">ضعیف</label>
                        <input type="radio" id="1" name="rate" value="1"/>
                    </div>
                    <div id="item">
                        <label for="2">متوسط</label>
                        <input type="radio" id="2" name="rate" value="2"/>
                    </div>
                    <div id="item">
                        <label for="3">خوب</label>
                        <input type="radio" id="3" name="rate" value="3"/>
                    </div>
                    <div id="item">
                        <label for="4">خیلی خوب</label>
                        <input type="radio" id="4" name="rate" value="4"/>
                    </div>
                    <div id="item">
                        <label for="5">عالی</label>
                        <input type="radio" id="5" name="rate" value="5"/>
                    </div>
                    <input type="submit" value="ثبت امتیاز">
                </form>
            </div>
        </div>
    `;
    fadeIn(frame);
    document.getElementById("closeBtn").addEventListener("click", ()=> fadeOut(frame));
}

function showMessage(text, fgcolor, bgcolor, fontsize, timeout){
    let frame = document.createElement('div');
    frame.id = "message";
    frame.innerHTML = text;
    frame.style.backgroundColor = bgcolor;
    frame.style.color = fgcolor;
    frame.style.fontSize = fontsize;
    fadeIn(frame);
    setTimeout(()=> fadeOut(frame), timeout);
}