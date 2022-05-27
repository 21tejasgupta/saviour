<!DOCTYPE HTML>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>Webcam</title>
</head>

<body onload="configure();">
    <div class="container">
        <div id="my_camera">
        </div>
    </div>
    <script type="text/javascript" src="assets/webcam.min.js">
    </script>
    <script type="text/javascript">
        function configure() {
            Webcam.set({
                width: 480,
                height: 360,
                image_format: 'jpeg',
                jpeg_quality: 90
            });

            Webcam.attatch('#my_camera');
        }
    </script>  
</body>
</html>