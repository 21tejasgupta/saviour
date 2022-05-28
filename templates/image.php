<?php
require 'templates\function.php';
?>

<!DOCTYPE HTML>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Image Database</title>
    </head>
<body>
    <table border=1 cellspacing=0 cellpadding=10>
        <tr>
            <td>#</td>
            <td>Date and Time</td>
            <td>Image</td>
        </tr>
        <?php
        $i=1;
        $rows=mysqli_query($conn,"SELECT * FROM tb_image ORDER BY id DESC");
        ?>
        <?php foreach($rows as $row): ?>
        <tr>
            <td><?php echo $i++; ?></td>
            <td><?php echo $row["date"]; ?></td>
            <td><img src="img/<?php echo $row["image"]; ?>" width=200 title="<?php echo $row["image"]; ?>" alt=""></td>
        </tr>
        <?php endforeach; ?>
    </table>
    <br>
    <a href="/capture"><button type="button" name="button">Go To Webcam page</button></a>
</body>
</html>
