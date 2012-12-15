define(['jquery', 'backbone', 'm/commit'], function($, Backbone, Commit) {
    var m = Backbone.Collection.extend({
        url: "https://api.github.com/users/chuck211991/events",
        model: Commit,
    });

    return m;
});
