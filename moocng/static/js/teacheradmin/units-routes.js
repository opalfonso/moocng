/*jslint vars: false, browser: true, nomen: true */
/*global MOOC:true, _, jQuery, Backbone */

// Copyright 2012 Rooter Analysis S.L.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

if (_.isUndefined(window.MOOC)) {
    window.MOOC = {};
}

(function ($, Backbone, _) {
    "use strict";

    var loadData = function (callback) {
        if (MOOC.models.course.length === 0) {
            // TODO
        }
        callback();
    };

    MOOC.App = Backbone.Router.extend({
        all: function () {
            var cb = function () {
                if (_.isUndefined(MOOC.views.listView)) {
                    MOOC.views.listView = new MOOC.views.List({
                        model: MOOC.models.course,
                        el: $("#units-container")[0]
                    });
                }

                MOOC.views.listView.render();
            };

            loadData(cb);
        },

        editUnit: function (unit) {
            var unitObj,
                unitView;

            unit = parseInt(unit, 10);
            unitView = MOOC.views.unitViews[unit];

            if (_.isUndefined(unitView)) {
                unitObj = MOOC.models.course.find(function (item) {
                    return unit === item.get("id");
                });
                unitView = new MOOC.views.Unit({
                    model: unitObj,
                    id: "unit" + unit,
                    el: $("#unit-editor")[0]
                });
                MOOC.views.unitViews[unit] = unitView;
            }

            unitView.render();
        },

        editKQ: function (kq) {
            var unitObj,
                kqObj,
                kqView;

            kq = parseInt(kq, 10);
            kqView = MOOC.views.kqViews[kq];

            if (_.isUndefined(kqView)) {
                unitObj = MOOC.models.course.getByKQ(kq);
                kqObj = unitObj.get("knowledgeQuantumList").find(function (item) {
                    return kq === item.get("id");
                });
                kqView = new MOOC.views.KQ({
                    model: kqObj,
                    id: "kq" + kq,
                    el: $("#kq-editor")[0]
                });
                MOOC.views.kqViews[kq] = kqView;
            }

            kqView.render();
        }
    });

    MOOC.init = function (courseID) {
        var path = window.location.pathname;

        MOOC.router = new MOOC.App();
        MOOC.router.route("", "all");
        MOOC.router.route("unit:unit", "editUnit");
        MOOC.router.route("kq:kq", "editKQ");

        if (path.lastIndexOf('/') < path.length - 1) {
            path += '/';
        }
        Backbone.history.start({ root: path });

        if (window.location.hash.length > 1) {
            path = window.location.hash.substring(1); // Remove #
            MOOC.router.navigate(path, { trigger: true });
        } else {
            MOOC.router.navigate("", { trigger: true });
        }
    };
}(jQuery, Backbone, _));