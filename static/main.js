$(document).ready(function(){
    var c = document.getElementById('canvas1');
    var ctx = c.getContext('2d');
    var bg = new Image();
    bg.src = background_file_name;
    ctx.drawImage(bg, 0, 0);
    
    var profile_image = new Image();
    profile_image.src=profile_image_url;
    ctx.drawImage(profile_image, 385, 150, 160, 160);

    ctx.font = "48px sans";
    ctx.textAlign='center';
    ctx.fillText(username, 460, 400);

    var grd=ctx.createLinearGradient(0,0,932,0);
    for (var i=0;i<color_list.length;++i){
        grd.addColorStop(color_list[i][0], color_list[i][1]);
    }
    ctx.fillStyle=grd;
    ctx.fillRect(0, 565, 932, 640);
});