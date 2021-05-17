$(document).ready(function() {
    $("#firstName").on('input', function() {
        id = $(this).attr("id");
        $("#firstNameError").text('');
        $("#firstName").removeClass("is-invalid");
    });

    $("#lastName").on('input', function() {
        id = $(this).attr("id");
        $("#lastNameError").text('');
        $("#lastName").removeClass("is-invalid");
    });

    $("#patronymic").on('input', function() {
        $("#patronymicError").text('');
        $("#patronymic").removeClass("is-invalid");
    });

    $("#login").on('input', function() {
        $("#loginError").text('');
        $("#login").removeClass("is-invalid");
    });

    $("#password").on('input', function() {
        $("#passwordError").text('');
        $("#password").removeClass("is-invalid");
    });
    
    $("#confirmPassword").on('input', function() {
        $("#confirmPasswordError").text('');
        $("#confirmPassword").removeClass("is-invalid");
    });

    $("#livingPlace").on('input', function() {
        $("#livingPlaceError").text('');
        $("#livingPlace").removeClass("is-invalid");
    });

    $("#email").on('input', function(event) {
        $(this).val(event.target.value);
        $("#emailError").text('').removeClass('text-warning').addClass('text-danger');;
        $("#email").removeClass("is-invalid");
        // $("#removeEmailIcon").removeClass("d-none");
    });

    $("#countryCode").on('input', function(event) {
        $(this).val(event.target.value);
        $("#countryCodeError").text('').removeClass('text-warning').addClass('text-danger');;
        $("#countryCode").removeClass("is-invalid");
        // $("#removeCountryCodeIcon").removeClass("d-none");
    });

    $("#phoneNumber").on('input', function() {
        $("#phoneNumberError").text('');
        $("#phoneNumber").removeClass("is-invalid");
    });

    $("#emailSelect[name='email']").on('change', function(event) {
        const iconClose = $(this).closest($("div[data-select-custom-enter='true']")).find(".custom-enter__icon-off");
        selected_email = $("#emailSelect option:selected").val();
        $("#emailError").text('');

        if (selected_email == "")
            $('#email').val('');
        else {
            $("#email").val(selected_email);
        }
        
        $("#email").removeClass("is-invalid");
        // $("#removeEmailIcon").removeClass("d-none");

        iconClose.on('click', function() {
            $("#emailError").text('Выберите email из списка или введите заново').removeClass('text-danger').addClass('text-warning');
        });
    });

    $("#countryCodeSelect[name='country_code']").on('change', function(event) {
        const iconClose = $(this).closest($("div[data-select-custom-enter='true']")).find(".custom-enter__icon-off");
        selected_email = $("#countryCodeSelect option:selected").val();
        $("#countryCodeError").text('');

        if (selected_email == "")
            $('#countryCode').val('');
        else {
            $("#countryCode").val(selected_email);
        }
        
        $("#countryCode").removeClass("is-invalid");
        // $("#removeCountryCodeIcon").removeClass("d-none");
        
        iconClose.on('click', function() {
            $("#countryCodeError").text('Выберите регион из списка или введите заново').removeClass('text-danger').addClass('text-warning');
        });
    });


    $("#input[name='email']").on('input', function(event) {
        $("#emailError").text('');
        $("#email").removeClass("is-invalid");
    });

    $("#birthday").on('input', function() {
        $("#birthdayError").text('');
        $("#birthday").removeClass("is-invalid");
    });

    $("#passportSeries").on('input', function() {
        $("#passportSeriesError").text('');
        $("#passportSeries").removeClass("is-invalid");
    });
    
    $("#passportNumber").on('input', function() {
        $("#passportNumberError").text('');
        $("#passportNumber").removeClass("is-invalid");
    });
    
    $("#foreignCitizenDoc").on('input', function() {
        $("#foreignCitizenDocError").text('');
        $("#foreignCitizenDoc").removeClass("is-invalid");
    });
    
    $("#passportAuthority").on('input', function() {
        $("#passportAuthorityError").text('');
        $("#passportAuthority").removeClass("is-invalid");
    });
    
    $("#passportDateIssue").on('input', function() {
        $("#passportDateIssueError").text('');
        $("#passportDateIssue").removeClass("is-invalid");
    });

    $("#changePasswordForm").validate({
        rules: {
            "password": {
                required: true
            },
            "confirm_password": {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            "password": {
                required: "Пожалуйста, введите пароль"
            },
            "confirm_password": {
                required: "Пожалуйста, подтвердите пароль",
                equalTo: "Введенные пароли не совпадают"
            }
        },
        submitHandler: function (form) {
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id
            $("#" + id + "Error").text(error[0].textContent)
        }
    });

    $("#registrationStep1Form").validate({
        rules: {
            "first_name": {
                required: true
            },
            "last_name": {
                required: true
            }
        },
        messages: {
            "first_name": {
                required: "Пожалуйста, введите имя"
            },
            "last_name": {
                required: "Пожалуйста, введите фамилию"
            }
        },
        submitHandler: function (form) {
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id;
            $("#" + id + "Error").text(error[0].textContent);
            $("#" + id).addClass("is-invalid");
        }
    });

    $("#registrationStep2Form").validate({
        rules: {
            "living_place": {
                required: true
            }
        },
        messages: {
            "living_place": {
                required: "Пожалуйста, укажите место жительства"
            }
        },
        submitHandler: function (form) {
            $("#birthday").val($("#birthday").val().split('/').reverse().join("-"));
            $("#passportDateIssue").val($("#passportDateIssue").val().split('/').reverse().join("-"));
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id;
            $("#" + id + "Error").text(error[0].textContent);
            $("#" + id).addClass("is-invalid");
        }
    });

    $("#loginForm").validate({
        rules: {
            "username": {
                required: true
            },
            "password": {
                required: true
            }
        },
        messages: {
            "username": {
                required: "Пожалуйста, введите логин"
            },
            "password": {
                required: "Пожалуйста, введите пароль"
            }
        },
        submitHandler: function (form) {
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id;
            $("#" + id + "Error").text(error[0].textContent);
            $("#" + id).addClass("is-invalid");
        }
    });

    $("#registrationParentStep3Form").validate({
        rules: {
            "email": {
                email: true,
                required: true
            },
            "phone_number": {
                required: true,
                minlength: 10,
                digits: true
            },
            "country_code": {
                required: true
            }
        },
        messages: {
            "email": {
                email: "Пожалуйста, введите корректный email-адрес",
                required: "Пожалуйста, введите email"
            },
            "phone_number": {
                required: "Пожалуйста, введите номер телефона",
                minlength: "Возможно Вы пропустили цифру",
                digits: "Разрешается ввод только цифр"
            },
            "country_code": {
                required: "Пожалуйста, введите код региона"
            }
        },
        submitHandler: function (form) {
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id;
            $("#" + id + "Error").text(error[0].textContent);
            $("#" + id).addClass("is-invalid");
            // $("#removeEmailIcon").addClass("d-none");
            // // $("#removeCountryCodeIcon").addClass("d-none");
        }
    });8

    $("#registrationStudentStep3Form").validate({
        rules: {
            "email": {
                email: true,
                required: true
            },
            "phone_number": {
                required: true,
                minlength: 10,
                digits: true
            },
            "country_code": {
                required: true
            },
            "birth_certificate": {
                required: true
            }
        },
        messages: {
            "email": {
                email: "Пожалуйста, введите корректный email-адрес",
                required: "Пожалуйста, введите email"
            },
            "phone_number": {
                required: "Пожалуйста, введите номер телефона",
                minlength: "Возможно Вы пропустили цифру",
                digits: "Разрешается ввод только цифр"
            },
            "country_code": {
                required: "Пожалуйста, введите код региона"
            }
        },
        submitHandler: function (form) {
            form.submit();
        },
        errorPlacement: function(error, element) {
            id = element[0].id;
            $("#" + id + "Error").text(error[0].textContent);
            $("#" + id).addClass("is-invalid");
            // $("#removeEmailIcon").addClass("d-none");
            // $("#removeCountryCodeIcon").addClass("d-none");
        }
    });

    $("label[id^=languageLabel]").click((event) => {
        $("#selectedLanguageBtn").text(event.target.textContent);
        var languageCode = event.target.attributes[1].value;
        $('#languageInput').val(languageCode);
        $('#languageForm').submit();
    });
})
