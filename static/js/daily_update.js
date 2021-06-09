document.getElementById('id_date').valueAsDate = new Date();
document.getElementById('id_date_to').valueAsDate = new Date();
document.getElementById('id_date_from').valueAsDate = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)

$(document).ready(function() {

        $(function() {
                $("form[name='daily_update']").validate({

                        rules: {
                            project: "required",

                            billable_hours: "required",
                            description_bh: "required",
                            non_billable_hours: "required",
                            description_nbh: "required",

                        }

                        ,

                        messages: {

                            project: "*Please select your project",
                            billable_hours: "*Please enter your billable hours",
                            non_billable_hours: "*Please enter your non billable hours",
                            submitHandler: function(form) {
                                form.submit();
                            }
                        }
                    }

                );
            }

        );

        var billable = 0;
        var non_billable = 0;

        $("#id_billable").on('change', function() {
                var getBillableTime = $("#id_billable").val().split(":");
                var hours = parseInt(getBillableTime[0]);
                var minutes = parseInt(getBillableTime[1]);
                billable = 60 * hours + minutes;

                $("#billable").val(billable);

            }

        );

        $("#id_non_billable").on('change', function() {
                var getNonBillableTime = $("#id_non_billable").val().split(":");
                var hours = parseInt(getNonBillableTime[0]);
                var minutes = parseInt(getNonBillableTime[1]);
                non_billable = 60 * hours + minutes;
                $("#non_billable").val(non_billable);

            }

        );


    }

);