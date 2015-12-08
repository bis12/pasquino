function descend(data, el) {
    el.empty()
    var ul = $("<ul>").appendTo(el);
    $.each(data, function(item, info){

        var state = info.state;
        var icon = "<i class='fa fa-question'></i>"

        if (state == "unscheduled") {
            icon = "<i class='fa fa-square-o'></i>"
        }
        else if (state == "scheduled") {
            icon = "<i class='fa fa-square'></i>"
        }
        else if (state == "completed") {
            icon = "<i class='fa fa-check-square success'></i>"
        }
        else if (state == "failed") {
            icon = "<i class='fa fa-minus-square warning'></i>"
        }
        else if (state == "exception") {
            icon = "<i class='fa fa-minus-square error'></i>"
        }
        var li = $("<li>").html(item + " " + icon);

        if (info.hasOwnProperty("children") && !($.isEmptyObject(info.children))) {
            descend(info.children, li);
        }
        ul.append(li);
    });
}

function populate(graphId, listType) {
    var path = "/task-graph/" + graphId + "/" + listType
    $("#tasklist").empty()
    $("#tasklist").append("<h2>Loading</h2>")
    $.getJSON(path, function(data) {
        descend(data, $("#tasklist"));
    });
}

$(document).ready(function() {
    $("#showList").click(function() {
        populate($("#graphId").val(), "states");
    });
    $("#showForest").click(function() {
        populate($("#graphId").val(), "forest");
    });
});
