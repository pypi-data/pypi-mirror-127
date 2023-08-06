$(function() {
    $(".sidebar-mini :input:not([type=checkbox]):not([type=button]):not([type=submit]):not([type=reset])").addClass("form-control");
    $(".has-error :input:not([type=checkbox]):not([type=button]):not([type=submit]):not([type=reset])").addClass("is-invalid");
});