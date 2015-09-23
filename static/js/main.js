$(document).ready(function(){ // Dom not loaded.must use ready event
    // no longer need to test if appadsa
    //alert("hi");

    $('form').submit(function(event){

        // We want to submit the form using Ajax (prevent page refresh)
        event.preventDefault();

        // This is where your validation code (if any) would go

        // ...

        // This tells the server-side process that Ajax was used
        $('input[name="usingAJAX"]', this).val('true');

        // Store reference to the form
        var $this = $(this);

        // Grabs the url from the form element
        var url = $this.attr('action');

        // Prepare the from to send
        //var dataToSend = $this.serialize();
        var dataToSend = JSON.stringify($this.serializeArray())

        // testing
        console.log(dataToSend);

        // The callback function that tells us what the server-side process had to say
        var callback = function(response){
            // hide the form (thankfully we stored a reference)
            $this.hide();

            //testing
            console.log(response);
            alert("callback");

            if (response == "success"){
            // do something
                alert("success");
            } else if(response == "fail"){
                alert("fail");
            }

            // Add logic to do when data has been received
            $('form').reset();

            //testing
            alert("testing");
        }

        // Add the rest later
        //$.post(url, dataToSend, callback, "json");

        $.ajax({
            type: "POST",
            url: url,
            data: dataToSend,
            success: function(response){
                alert("success!!!");
            },
            dataType: "json"
        });


        // Clears the form
        // Should be called if the ajax request was successful...
