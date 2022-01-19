function read() {
/* var x = document.getElementById("img").src;*/

    var x = $("#txturl").val();
    if (x === '') {
       document.getElementById('Resultnotfounr').style.display = "none";
      /* alert('hello')*/
    } else{
            var e = {
            async: !0,
            crossDomain: !0,
            url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/url",
            method: "POST",
            headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "content-type": "application/json", "cache-control": "no-cache", "postman-token": "a8ca2ede-75df-f164-20fb-e5f08fa71b51" },
            processData: !1,
            data: '{"Url":"' + ($("#txturl").val() + '" }'),
        };
        $.ajax(e).done(function (e) {
            var t,
                i = 0;
            Object.keys(e.predictions).length;
            $(e.predictions).each(function (e, n) {
                n.probability > i && ((i = n.probability), (t = n.tagName));
            }),
                (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
                (document.getElementById("lblname").innerText = t),
                console.log(i),
                console.log(t);
document.getElementById('Resultnotfounr').style.display = "block";
document.getElementById("img").src = $("#txturl").val();
        }).fail(function(){
document.getElementById('Resultnotfounr').style.display = "none";
})
 
    }
}




function read1(a){
    console.log(a.src);
         document.getElementById('Resultnotfounr').style.display = "block";
    document.getElementById("img").src = a.src;
    var e = {
        async: !0,
        crossDomain: !0,
        url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/url",
        method: "POST",
        headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "content-type": "application/json", "cache-control": "no-cache", "postman-token": "a8ca2ede-75df-f164-20fb-e5f08fa71b51" },
        processData: !1,
        data: '{"Url":"' + (a.src + '" }'),
    };
    $.ajax(e).done(function (e) {
        var t,
            i = 0;
        Object.keys(e.predictions).length;
        $(e.predictions).each(function (e, n) {
            n.probability > i && ((i = n.probability), (t = n.tagName));
        }),
            (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
            (document.getElementById("lblname").innerText = t),
            console.log(i),
            console.log(t);
    });
}

$(function () {

    $("#upload").change(function () {
        document.getElementById('Resultnotfounr').style.display = "block";
        var e = $(this).val(),
            t = e.substring(e.lastIndexOf(".") + 1).toLowerCase();
        if (this.files && this.files[0] && ("gif" == t || "png" == t || "jpeg" == t || "jpg" == t)) {
            this.files[0];
            var i = new FileReader();
            i.addEventListener("load", function (e) {
                $("#img").attr("src", e.target.result);
                for (var t = atob(e.target.result.split(",")[1]), i = new ArrayBuffer(t.length), n = new Uint8Array(i), o = 0; o < t.length; o++) n[o] = 255 & t.charCodeAt(o);
                var a = {
                    async: !0,
                    crossDomain: !0,
                    url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/image",
                    method: "POST",
                    headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "Content-Type": "application/octet-stream", "cache-control": "no-cache" },
                    processData: !1,
                    data: n,
                };
                $.ajax(a).done(function (e) {
                    var t,
                        i = 0;
                    Object.keys(e.predictions).length;
                    $(e.predictions).each(function (e, n) {
                        n.probability > i && ((i = n.probability), (t = n.tagName));
                    }),
                        (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
                        (document.getElementById("lblname").innerText = t);
                });
            }),
                i.readAsDataURL(this.files[0]);
            var n = this.files[0].mozFullPath;
            /*console.log(n);*/
        } /*else $("#img").attr("src", "/assets/no_preview.png");*/
    });
});


/*function read() {
  document.getElementById("img").src = $("#txturl").val();
    var e = {
        async: !0,
        crossDomain: !0,
        url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/url",
        method: "POST",
        headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "content-type": "application/json", "cache-control": "no-cache", "postman-token": "a8ca2ede-75df-f164-20fb-e5f08fa71b51" },
        processData: !1,
        data: '{"Url":"' + ($("#txturl").val() + '" }'),
    };
    $.ajax(e).done(function (e) {
        var t,
            i = 0;
        Object.keys(e.predictions).length;
        $(e.predictions).each(function (e, n) {
            n.probability > i && ((i = n.probability), (t = n.tagName));
        }),
            (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
            (document.getElementById("lblname").innerText = t),
            console.log(i),
            console.log(t);
    });
}




function read1(a){
    console.log(a.src);
         
        document.getElementById("img").src = a.src;
    var e = {
        async: !0,
        crossDomain: !0,
        url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/url",
        method: "POST",
        headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "content-type": "application/json", "cache-control": "no-cache", "postman-token": "a8ca2ede-75df-f164-20fb-e5f08fa71b51" },
        processData: !1,
        data: '{"Url":"' + (a.src + '" }'),
    };
    $.ajax(e).done(function (e) {
        var t,
            i = 0;
        Object.keys(e.predictions).length;
        $(e.predictions).each(function (e, n) {
            n.probability > i && ((i = n.probability), (t = n.tagName));
        }),
            (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
            (document.getElementById("lblname").innerText = t),
            console.log(i),
            console.log(t);
    });
}

$(function () {
    $("#upload").change(function () {
        var e = $(this).val(),
            t = e.substring(e.lastIndexOf(".") + 1).toLowerCase();
        if (this.files && this.files[0] && ("gif" == t || "png" == t || "jpeg" == t || "jpg" == t)) {
            this.files[0];
            var i = new FileReader();
            i.addEventListener("load", function (e) {
                $("#img").attr("src", e.target.result);
                for (var t = atob(e.target.result.split(",")[1]), i = new ArrayBuffer(t.length), n = new Uint8Array(i), o = 0; o < t.length; o++) n[o] = 255 & t.charCodeAt(o);
                var a = {
                    async: !0,
                    crossDomain: !0,
                    url: "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8d324c0a-be75-465a-b261-3567f7a81f28/classify/iterations/Bird%20Species%20Recognition/image",
                    method: "POST",
                    headers: { "prediction-key": "4c980ee7e366481482621ce843ec996b", "Content-Type": "application/octet-stream", "cache-control": "no-cache" },
                    processData: !1,
                    data: n,
                };
                $.ajax(a).done(function (e) {
                    var t,
                        i = 0;
                    Object.keys(e.predictions).length;
                    $(e.predictions).each(function (e, n) {
                        n.probability > i && ((i = n.probability), (t = n.tagName));
                    }),
                        (document.getElementById("lblprediction").innerText = (100 * i).toFixed(2) + "%"),
                        (document.getElementById("lblname").innerText = t);
                });
            }),
                i.readAsDataURL(this.files[0]);
            var n = this.files[0].mozFullPath;
            console.log(n);
        } else $("#img").attr("src", "/assets/no_preview.png");
    });
});
*/


