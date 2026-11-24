/* Restores the saved viewer theme (standard or shoreline) before the first
 * paint. The header select that changes it is wired in app.js; unusable or
 * missing values stay on the standard theme, which follows the OS setting. */
(function () {
  "use strict";
  try {
    if (localStorage.getItem("devlog.theme") === "shore") {
      document.documentElement.setAttribute("data-theme", "shore");
    }
  } catch (e) { /* storage unavailable: standard theme */ }
})();
