var featureRequestModel = {
    featureTitle: ko.observable(""),
    featureDescription: ko.observable(""),
    clientValues: [
        { name: "Client A", id: "A" },
        { name: "Client B", id: "B" },
        { name: "Client C", id: "C" }
    ],
    selectedClient: ko.observable(1),
    priority: ko.observable(1),
    target: ko.observable(moment().format("YYYY-MM-DD")),
    areaValues: [
        { name: "Policies", id: "Policies" },
        { name: "Billings", id: "Billings" },
        { name: "Claims", id: "Claims" },
        { name: "Reports", id: "Reports" }
    ],
    selectedArea: ko.observable('policy'),
    create: function (formElement) {
        $(formElement).validate();
        $.ajax({
            url: '/createFeature',
            data: $(formElement).serialize(),
            type: 'POST',
            success: function (response) {
                window.location = "/";
            },
            error: function (error) {
                console.log(error);
            }
        });
    },
    deleteFeature: function (id, data, event) {
        $.ajax({
            url: '/delete/' + id,
            type: 'DELETE',
            success: function (response) {
                window.location = "/";
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
};
ko.applyBindings(featureRequestModel, document.getElementById("createFeature"));