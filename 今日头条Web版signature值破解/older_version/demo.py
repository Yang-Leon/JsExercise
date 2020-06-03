#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import execjs
import requests

toutiaohao_sign_js = """
//window.TAC && (console.log(userInfo.id + "" + a[t]),
window = {};
global.navigator = {};
global.navigator.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36";

function getAsCp() {
    function t(e, t) {
        var n = (65535 & e) + (65535 & t)
            , r = (e >> 16) + (t >> 16) + (n >> 16);
        return r << 16 | 65535 & n
    }

    function n(e, t) {
        return e << t | e >>> 32 - t
    }

    function r(e, r, o, i, u, a) {
        return t(n(t(t(r, e), t(i, a)), u), o)
    }

    function o(e, t, n, o, i, u, a) {
        return r(t & n | ~t & o, e, t, i, u, a)
    }

    function i(e, t, n, o, i, u, a) {
        return r(t & o | n & ~o, e, t, i, u, a)
    }

    function u(e, t, n, o, i, u, a) {
        return r(t ^ n ^ o, e, t, i, u, a)
    }

    function a(e, t, n, o, i, u, a) {
        return r(n ^ (t | ~o), e, t, i, u, a)
    }

    function s(e, n) {
        e[n >> 5] |= 128 << n % 32,
            e[(n + 64 >>> 9 << 4) + 14] = n;
        var r, s, c, l, f, p = 1732584193, d = -271733879, h = -1732584194, m = 271733878;
        for (r = 0; r < e.length; r += 16)
            s = p,
                c = d,
                l = h,
                f = m,
                p = o(p, d, h, m, e[r], 7, -680876936),
                m = o(m, p, d, h, e[r + 1], 12, -389564586),
                h = o(h, m, p, d, e[r + 2], 17, 606105819),
                d = o(d, h, m, p, e[r + 3], 22, -1044525330),
                p = o(p, d, h, m, e[r + 4], 7, -176418897),
                m = o(m, p, d, h, e[r + 5], 12, 1200080426),
                h = o(h, m, p, d, e[r + 6], 17, -1473231341),
                d = o(d, h, m, p, e[r + 7], 22, -45705983),
                p = o(p, d, h, m, e[r + 8], 7, 1770035416),
                m = o(m, p, d, h, e[r + 9], 12, -1958414417),
                h = o(h, m, p, d, e[r + 10], 17, -42063),
                d = o(d, h, m, p, e[r + 11], 22, -1990404162),
                p = o(p, d, h, m, e[r + 12], 7, 1804603682),
                m = o(m, p, d, h, e[r + 13], 12, -40341101),
                h = o(h, m, p, d, e[r + 14], 17, -1502002290),
                d = o(d, h, m, p, e[r + 15], 22, 1236535329),
                p = i(p, d, h, m, e[r + 1], 5, -165796510),
                m = i(m, p, d, h, e[r + 6], 9, -1069501632),
                h = i(h, m, p, d, e[r + 11], 14, 643717713),
                d = i(d, h, m, p, e[r], 20, -373897302),
                p = i(p, d, h, m, e[r + 5], 5, -701558691),
                m = i(m, p, d, h, e[r + 10], 9, 38016083),
                h = i(h, m, p, d, e[r + 15], 14, -660478335),
                d = i(d, h, m, p, e[r + 4], 20, -405537848),
                p = i(p, d, h, m, e[r + 9], 5, 568446438),
                m = i(m, p, d, h, e[r + 14], 9, -1019803690),
                h = i(h, m, p, d, e[r + 3], 14, -187363961),
                d = i(d, h, m, p, e[r + 8], 20, 1163531501),
                p = i(p, d, h, m, e[r + 13], 5, -1444681467),
                m = i(m, p, d, h, e[r + 2], 9, -51403784),
                h = i(h, m, p, d, e[r + 7], 14, 1735328473),
                d = i(d, h, m, p, e[r + 12], 20, -1926607734),
                p = u(p, d, h, m, e[r + 5], 4, -378558),
                m = u(m, p, d, h, e[r + 8], 11, -2022574463),
                h = u(h, m, p, d, e[r + 11], 16, 1839030562),
                d = u(d, h, m, p, e[r + 14], 23, -35309556),
                p = u(p, d, h, m, e[r + 1], 4, -1530992060),
                m = u(m, p, d, h, e[r + 4], 11, 1272893353),
                h = u(h, m, p, d, e[r + 7], 16, -155497632),
                d = u(d, h, m, p, e[r + 10], 23, -1094730640),
                p = u(p, d, h, m, e[r + 13], 4, 681279174),
                m = u(m, p, d, h, e[r], 11, -358537222),
                h = u(h, m, p, d, e[r + 3], 16, -722521979),
                d = u(d, h, m, p, e[r + 6], 23, 76029189),
                p = u(p, d, h, m, e[r + 9], 4, -640364487),
                m = u(m, p, d, h, e[r + 12], 11, -421815835),
                h = u(h, m, p, d, e[r + 15], 16, 530742520),
                d = u(d, h, m, p, e[r + 2], 23, -995338651),
                p = a(p, d, h, m, e[r], 6, -198630844),
                m = a(m, p, d, h, e[r + 7], 10, 1126891415),
                h = a(h, m, p, d, e[r + 14], 15, -1416354905),
                d = a(d, h, m, p, e[r + 5], 21, -57434055),
                p = a(p, d, h, m, e[r + 12], 6, 1700485571),
                m = a(m, p, d, h, e[r + 3], 10, -1894986606),
                h = a(h, m, p, d, e[r + 10], 15, -1051523),
                d = a(d, h, m, p, e[r + 1], 21, -2054922799),
                p = a(p, d, h, m, e[r + 8], 6, 1873313359),
                m = a(m, p, d, h, e[r + 15], 10, -30611744),
                h = a(h, m, p, d, e[r + 6], 15, -1560198380),
                d = a(d, h, m, p, e[r + 13], 21, 1309151649),
                p = a(p, d, h, m, e[r + 4], 6, -145523070),
                m = a(m, p, d, h, e[r + 11], 10, -1120210379),
                h = a(h, m, p, d, e[r + 2], 15, 718787259),
                d = a(d, h, m, p, e[r + 9], 21, -343485551),
                p = t(p, s),
                d = t(d, c),
                h = t(h, l),
                m = t(m, f);
        return [p, d, h, m]
    }

    function c(e) {
        var t, n = "";
        for (t = 0; t < 32 * e.length; t += 8)
            n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
        return n
    }

    function l(e) {
        var t, n = [];
        for (n[(e.length >> 2) - 1] = void 0,
                 t = 0; t < n.length; t += 1)
            n[t] = 0;
        for (t = 0; t < 8 * e.length; t += 8)
            n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
        return n
    }

    function f(e) {
        return c(s(l(e), 8 * e.length))
    }

    function p(e, t) {
        var n, r, o = l(e), i = [], u = [];
        for (i[15] = u[15] = void 0,
             o.length > 16 && (o = s(o, 8 * e.length)),
                 n = 0; 16 > n; n += 1)
            i[n] = 909522486 ^ o[n],
                u[n] = 1549556828 ^ o[n];
        return r = s(i.concat(l(t)), 512 + 8 * t.length),
            c(s(u.concat(r), 640))
    }

    function d(e) {
        var t, n, r = "0123456789abcdef", o = "";
        for (n = 0; n < e.length; n += 1)
            t = e.charCodeAt(n),
                o += r.charAt(t >>> 4 & 15) + r.charAt(15 & t);
        return o
    }

    function h(e) {
        return unescape(encodeURIComponent(e))
    }

    function m(e) {
        return f(h(e))
    }

    function g(e) {
        return d(m(e))
    }

    function v(e, t) {
        return p(h(e), h(t))
    }

    function y(e, t) {
        return d(v(e, t))
    }

    function b(e, t, n) {
        return t ? n ? v(t, e) : y(t, e) : n ? m(e) : g(e)
    }

    function getHoney() {
        var t = Math.floor((new Date).getTime() / 1e3),
            e = t.toString(16).toUpperCase(),
            n = b(t, null, null).toString().toUpperCase();
        if (8 != e.length) return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
        for (var o = n.slice(0, 5), i = n.slice(-5), a = "", r = 0; 5 > r; r++) a += o[r] + e[r];
        for (var l = "", s = 0; 5 > s; s++) l += e[s + 3] + i[s];
        return {
            as: "A1" + a + e.slice(-3),
            cp: e.slice(0, 3) + l + "E1"
        }
    }

    return getHoney()
}

function asd() {
    function e(e, a, r) {
        return (b[e] || (b[e] = t("x,y", "return x " + e + " y")))(r, a)
    }

    function a(e, a, r) {
        return (k[r] || (k[r] = t("x,y", "return new x[y](" + Array(r + 1).join(",x[++y]").substr(1) + ")")))(e, a)
    }

    function r(e, a, r) {
        var n, t, s = {}, b = s.d = r ? r.d + 1 : 0;
        for (s["$" + b] = s,
                 t = 0; t < b; t++)
            s[n = "$" + t] = r[n];
        for (t = 0,
                 b = s.length = a.length; t < b; t++)
            s[t] = a[t];
        return c(e, 0, s)
    }

    function c(t, b, k) {
        function u(e) {
            v[x++] = e
        }

        function f() {
            return g = t.charCodeAt(b++) - 32,
                t.substring(b, b += g)
        }

        function l() {
            try {
                y = c(t, b, k)
            } catch (e) {
                h = e,
                    y = l
            }
        }

        for (var h, y, d, g, v = [], x = 0; ;)
            switch (g = t.charCodeAt(b++) - 32) {
                case 1:
                    u(!v[--x]);
                    break;
                case 4:
                    v[x++] = f();
                    break;
                case 5:
                    u(function (e) {
                        var a = 0
                            , r = e.length;
                        return function () {
                            var c = a < r;
                            return c && u(e[a++]),
                                c
                        }
                    }(v[--x]));
                    break;
                case 6:
                    y = v[--x],
                        u(v[--x](y));
                    break;
                case 8:
                    if (g = t.charCodeAt(b++) - 32,
                        l(),
                        b += g,
                        g = t.charCodeAt(b++) - 32,
                    y === c)
                        b += g;
                    else if (y !== l)
                        return y;
                    break;
                case 9:
                    v[x++] = c;
                    break;
                case 10:
                    u(s(v[--x]));
                    break;
                case 11:
                    y = v[--x],
                        u(v[--x] + y);
                    break;
                case 12:
                    for (y = f(),
                             d = [],
                             g = 0; g < y.length; g++)
                        d[g] = y.charCodeAt(g) ^ g + y.length;
                    u(String.fromCharCode.apply(null, d));
                    break;
                case 13:
                    y = v[--x],
                        h = delete v[--x][y];
                    break;
                case 14:
                    v[x++] = t.charCodeAt(b++) - 32;
                    break;
                case 59:
                    u((g = t.charCodeAt(b++) - 32) ? (y = x,
                        v.slice(x -= g, y)) : []);
                    break;
                case 61:
                    u(v[--x][t.charCodeAt(b++) - 32]);
                    break;
                case 62:
                    g = v[--x],
                        k[0] = 65599 * k[0] + k[1].charCodeAt(g) >>> 0;
                    break;
                case 65:
                    h = v[--x],
                        y = v[--x],
                        v[--x][y] = h;
                    break;
                case 66:
                    u(e(t[b++], v[--x], v[--x]));
                    break;
                case 67:
                    y = v[--x],
                        d = v[--x],
                        u((g = v[--x]).x === c ? r(g.y, y, k) : g.apply(d, y));
                    break;
                case 68:
                    u(e((g = t[b++]) < "<" ? (b--,
                        f()) : g + g, v[--x], v[--x]));
                    break;
                case 70:
                    u(!1);
                    break;
                case 71:
                    v[x++] = n;
                    break;
                case 72:
                    v[x++] = +f();
                    break;
                case 73:
                    u(parseInt(f(), 36));
                    break;
                case 75:
                    if (v[--x]) {
                        b++;
                        break
                    }
                case 74:
                    g = t.charCodeAt(b++) - 32 << 16 >> 16,
                        b += g;
                    break;
                case 76:
                    u(k[t.charCodeAt(b++) - 32]);
                    break;
                case 77:
                    y = v[--x],
                        u(v[--x][y]);
                    break;
                case 78:
                    g = t.charCodeAt(b++) - 32,
                        u(a(v, x -= g + 1, g));
                    break;
                case 79:
                    g = t.charCodeAt(b++) - 32,
                        u(k["$" + g]);
                    break;
                case 81:
                    h = v[--x],
                        v[--x][f()] = h;
                    break;
                case 82:
                    u(v[--x][f()]);
                    break;
                case 83:
                    h = v[--x],
                        k[t.charCodeAt(b++) - 32] = h;
                    break;
                case 84:
                    v[x++] = !0;
                    break;
                case 85:
                    v[x++] = void 0;
                    break;
                case 86:
                    u(v[x - 1]);
                    break;
                case 88:
                    h = v[--x],
                        y = v[--x],
                        v[x++] = h,
                        v[x++] = y;
                    break;
                case 89:
                    u(function () {
                        function e() {
                            return r(e.y, arguments, k)
                        }

                        return e.y = f(),
                            e.x = c,
                            e
                    }());
                    break;
                case 90:
                    v[x++] = null;
                    break;
                case 91:
                    v[x++] = h;
                    break;
                case 93:
                    h = v[--x];
                    break;
                case 0:
                    return v[--x];
                default:
                    u((g << 16 >> 16) - 16)
            }
    }

    var n = this
        , t = n.Function
        , s = Object.keys || function (e) {
        var a = {}
            , r = 0;
        for (var c in e)
            a[r++] = c;
        return a.length = r,
            a
    }
        , b = {}
        , k = {};

    var r_param_e_str = String.fromCharCode(103, 114, 36, 68, 97, 116, 101, 110, 32, 1048, 98, 47, 115, 33, 108, 32, 121, 850, 121, 313, 103, 44, 40, 108, 102, 105, 126, 97, 104, 96, 123, 109, 118, 44, 45, 110, 124, 106, 113, 101, 119, 86, 120, 112, 123, 114, 118, 109, 109, 120, 44, 38, 101, 102, 102, 127, 107, 120, 91, 33, 99, 115, 34, 108, 34, 46, 80, 113, 37, 119, 105, 100, 116, 104, 108, 34, 64, 113, 38, 104, 101, 105, 103, 104, 116, 108, 34, 118, 114, 42, 103, 101, 116, 67, 111, 110, 116, 101, 120, 116, 120, 36, 34, 50, 100, 91, 33, 99, 115, 35, 108, 35, 44, 42, 59, 63, 124, 117, 46, 124, 117, 99, 123, 117, 113, 36, 102, 111, 110, 116, 108, 35, 118, 114, 40, 102, 105, 108, 108, 84, 101, 120, 116, 120, 36, 36, 40856, 3601, 3616, 44221, 50, 60, 91, 35, 99, 125, 108, 35, 50, 113, 42, 115, 104, 97, 100, 111, 119, 66, 108, 117, 114, 108, 35, 49, 113, 45, 115, 104, 97, 100, 111, 119, 79, 102, 102, 115, 101, 116, 88, 108, 35, 36, 36, 108, 105, 109, 101, 113, 43, 115, 104, 97, 100, 111, 119, 67, 111, 108, 111, 114, 108, 35, 118, 114, 35, 97, 114, 99, 120, 56, 56, 56, 48, 50, 91, 37, 99, 125, 108, 35, 118, 114, 38, 115, 116, 114, 111, 107, 101, 120, 91, 32, 99, 125, 108, 34, 118, 44, 41, 125, 101, 79, 109, 121, 111, 90, 66, 93, 109, 120, 91, 32, 99, 115, 33, 48, 115, 36, 108, 36, 80, 98, 60, 107, 55, 108, 32, 108, 33, 114, 38, 108, 101, 110, 103, 116, 104, 98, 37, 94, 108, 36, 49, 43, 115, 36, 106, 2, 108, 32, 32, 115, 35, 105, 36, 49, 101, 107, 49, 115, 36, 103, 114, 35, 116, 97, 99, 107, 52, 41, 122, 103, 114, 35, 116, 97, 99, 36, 33, 32, 43, 48, 111, 33, 91, 35, 99, 106, 63, 111, 32, 93, 33, 108, 36, 98, 37, 115, 34, 111, 32, 93, 33, 108, 34, 108, 36, 98, 42, 98, 94, 48, 100, 35, 62, 62, 62, 115, 33, 48, 115, 37, 121, 65, 48, 115, 34, 108, 34, 108, 33, 114, 38, 108, 101, 110, 103, 116, 104, 98, 60, 107, 43, 108, 34, 94, 108, 34, 49, 43, 115, 34, 106, 5, 108, 32, 32, 115, 38, 108, 38, 122, 48, 108, 33, 36, 32, 43, 91, 34, 99, 115, 39, 40, 48, 108, 35, 105, 39, 49, 112, 115, 57, 119, 120, 98, 38, 115, 40, 41, 32, 38, 123, 115, 41, 47, 115, 40, 103, 114, 38, 83, 116, 114, 105, 110, 103, 114, 44, 102, 114, 111, 109, 67, 104, 97, 114, 67, 111, 100, 101, 115, 41, 48, 115, 42, 121, 87, 108, 32, 46, 95, 98, 38, 115, 32, 111, 33, 93, 41, 108, 32, 108, 32, 74, 98, 60, 107, 36, 46, 97, 106, 59, 108, 32, 46, 84, 98, 60, 107, 36, 46, 103, 106, 47, 108, 32, 46, 94, 98, 60, 107, 38, 105, 34, 45, 52, 106, 33, 31, 43, 38, 32, 115, 43, 121, 80, 111, 33, 93, 43, 115, 33, 108, 33, 108, 32, 72, 100, 62, 38, 108, 33, 108, 32, 66, 100, 62, 38, 43, 108, 33, 108, 32, 60, 100, 62, 38, 43, 108, 33, 108, 32, 54, 100, 62, 38, 43, 108, 33, 108, 32, 38, 43, 32, 115, 44, 121, 61, 111, 33, 111, 33, 93, 47, 113, 34, 49, 51, 111, 33, 108, 32, 113, 34, 49, 48, 111, 33, 93, 44, 108, 32, 50, 100, 62, 38, 32, 115, 46, 123, 115, 45, 121, 77, 111, 33, 111, 33, 93, 48, 113, 34, 49, 51, 111, 33, 93, 42, 76, 100, 60, 108, 32, 52, 100, 35, 62, 62, 62, 98, 124, 115, 33, 111, 33, 108, 32, 113, 34, 49, 48, 111, 33, 93, 44, 108, 33, 38, 32, 115, 47, 121, 73, 111, 33, 111, 33, 93, 46, 113, 34, 49, 51, 111, 33, 93, 44, 111, 33, 93, 42, 74, 100, 60, 108, 32, 54, 100, 35, 62, 62, 62, 98, 124, 38, 111, 33, 93, 43, 108, 32, 38, 43, 32, 115, 48, 108, 45, 108, 33, 38, 108, 45, 108, 33, 105, 39, 49, 122, 49, 52, 49, 122, 52, 98, 47, 64, 100, 60, 108, 34, 98, 124, 38, 43, 108, 45, 108, 40, 108, 33, 98, 94, 38, 43, 108, 45, 108, 38, 122, 108, 39, 103, 44, 41, 103, 107, 125, 101, 106, 111, 123, 127, 99, 109, 44, 41, 124, 121, 110, 126, 76, 105, 106, 126, 101, 109, 91, 34, 99, 108, 36, 98, 37, 64, 100, 60, 108, 38, 122, 108, 39, 108, 32, 36, 32, 43, 91, 34, 99, 108, 36, 98, 37, 98, 124, 38, 43, 108, 45, 108, 37, 56, 100, 60, 64, 98, 124, 108, 33, 98, 94, 38, 43, 32, 113, 36, 115, 105, 103, 110, 32);
    r(r_param_e_str, [TAC = {}]);
}

function getSign(mid, max_behot_time) {
    asd();
    return TAC.sign(mid + "" + max_behot_time);
}


function getParams(mid, max_behot_time) {
    var as_cp = getAsCp();
    var _signature = getSign(mid, max_behot_time);
    return {
        as: as_cp['as'],
        cp: as_cp['cp'],
        _signature: _signature,
    }
}

// console.log(getParams(4157040672, 0));

"""


def get_params(mid, max_behot_time=0):
    node = execjs.get()
    # ctx = node.compile(open('encryption.js', 'r', encoding='gbk').read())
    ctx = node.compile(toutiaohao_sign_js)
    p = ctx.call('getParams', mid, max_behot_time)
    print(json.dumps(p, indent=4, ensure_ascii=False))
    return p


def get_data(mid, p, max_behot_time=0):
    headers = {
        "accept": "application/json, text/javascript",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "referer": "https://www.toutiao.com/c/user/{}/".format(mid),
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    params = {
        # 0：视频，1：文章，
        "page_type": 1,
        "user_id": mid,
        "max_behot_time": max_behot_time,
        "count": 20,
        "as": p['as'],
        "cp": p['cp'],
        "_signature": p['_signature'],
    }
    response = requests.get('https://www.toutiao.com/c/user/article/', headers=headers, params=params)
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    # mid = 52900120370
    mid = 4060783862
    max_behot_time = 0
    p = get_params(mid, max_behot_time)
    get_data(mid, p, max_behot_time)
