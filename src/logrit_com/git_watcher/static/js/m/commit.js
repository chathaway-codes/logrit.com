define(['jquery', 'backbone'], function($, Backbone) {
    var m = Backbone.Model.extend({
        getCommits: function() {
            if(this.get("type") != "PushEvent")
                return [];
            return this.get("payload").commits;
        },
    });

    return m;
});
