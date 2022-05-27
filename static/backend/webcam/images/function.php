<?php

$conn=mysqli_connect("localhost","root","","webcam");

if(isset($_FILES["webcam"]["temp_name"])){
    $tempName=$_FILES["webcam"]["tmp_name"];
    $imageName=date("Y.m.d")."-".date("h.i.sa").'.jpeg';
    move_uploaded_file($tmpName,'images/'.$imageName);

    $date=date("Y/m/d")."&".date("h:i:sa");
    $query="INSERT INTO tb_image VALUES('','$date','$imageName')";
    mysqli_query($conn,$query);
}
?>