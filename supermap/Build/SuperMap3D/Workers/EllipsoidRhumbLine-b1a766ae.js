define(["exports","./Cartesian3-3a8bdb0b","./Cartographic-a2c313d7","./Check-52a7d806","./when-92c6cf3c","./Cartesian2-b72655a5","./Math-ecf82623"],(function(t,i,e,a,n,s,h){"use strict";function o(t,i,e){if(0===t)return i*e;var a=t*t,n=a*a,s=n*a,h=s*a,o=h*a,r=o*a,d=e;return i*((1-a/4-3*n/64-5*s/256-175*h/16384-441*o/65536-4851*r/1048576)*d-(3*a/8+3*n/32+45*s/1024+105*h/4096+2205*o/131072+6237*r/524288)*Math.sin(2*d)+(15*n/256+45*s/1024+525*h/16384+1575*o/65536+155925*r/8388608)*Math.sin(4*d)-(35*s/3072+175*h/12288+3675*o/262144+13475*r/1048576)*Math.sin(6*d)+(315*h/131072+2205*o/524288+43659*r/8388608)*Math.sin(8*d)-(693*o/1310720+6237*r/5242880)*Math.sin(10*d)+1001*r/8388608*Math.sin(12*d))}function r(t,i){if(0===t)return Math.log(Math.tan(.5*(h.e.PI_OVER_TWO+i)));var e=t*Math.sin(i);return Math.log(Math.tan(.5*(h.e.PI_OVER_TWO+i)))-t/2*Math.log((1+e)/(1-e))}var d=new i.o,u=new i.o;function l(t,n,s,l){var c=i.o.normalize(l.cartographicToCartesian(n,u),d),_=i.o.normalize(l.cartographicToCartesian(s,u),u);a.o.typeOf.number.greaterThanOrEquals("value",Math.abs(Math.abs(i.o.angleBetween(c,_))-Math.PI),.0125);var g=l.maximumRadius,M=l.minimumRadius,f=g*g,p=M*M;t._ellipticitySquared=(f-p)/f,t._ellipticity=Math.sqrt(t._ellipticitySquared),t._start=e.a.clone(n,t._start),t._start.height=0,t._end=e.a.clone(s,t._end),t._end.height=0,t._heading=function(t,i,e,a,n){var s=r(t._ellipticity,e),o=r(t._ellipticity,n);return Math.atan2(h.e.negativePiToPi(a-i),o-s)}(t,n.longitude,n.latitude,s.longitude,s.latitude),t._distance=function(t,i,e,a,n,s,r){var d=t._heading,u=s-a,l=0;if(h.e.equalsEpsilon(Math.abs(d),h.e.PI_OVER_TWO,h.e.EPSILON8))if(i===e)l=i*Math.cos(n)*h.e.negativePiToPi(u);else{var c=Math.sin(n);l=i*Math.cos(n)*h.e.negativePiToPi(u)/Math.sqrt(1-t._ellipticitySquared*c*c)}else{var _=o(t._ellipticity,i,n);l=(o(t._ellipticity,i,r)-_)/Math.cos(d)}return Math.abs(l)}(t,l.maximumRadius,l.minimumRadius,n.longitude,n.latitude,s.longitude,s.latitude)}function c(t,i,a,s,d,u){var l,c,_,g=d*d;if(Math.abs(h.e.PI_OVER_TWO-Math.abs(i))>h.e.EPSILON8){c=function(t,i,e){var a=t/e;if(0===i)return a;var n=a*a,s=n*a,h=s*a,o=i*i,r=o*o,d=r*o,u=d*o,l=u*o,c=l*o,_=Math.sin(2*a),g=Math.cos(2*a),M=Math.sin(4*a),f=Math.cos(4*a),p=Math.sin(6*a),P=Math.cos(6*a),v=Math.sin(8*a),O=Math.cos(8*a),m=Math.sin(10*a);return a+a*o/4+7*a*r/64+15*a*d/256+579*a*u/16384+1515*a*l/65536+16837*a*c/1048576+(3*a*r/16+45*a*d/256-a*(32*n-561)*u/4096-a*(232*n-1677)*l/16384+a*(399985-90560*n+512*h)*c/5242880)*g+(21*a*d/256+483*a*u/4096-a*(224*n-1969)*l/16384-a*(33152*n-112599)*c/1048576)*f+(151*a*u/4096+4681*a*l/65536+1479*a*c/16384-453*s*c/32768)*P+(1097*a*l/65536+42783*a*c/1048576)*O+8011*a*c/1048576*Math.cos(10*a)+(3*o/8+3*r/16+213*d/2048-3*n*d/64+255*u/4096-33*n*u/512+20861*l/524288-33*n*l/512+h*l/1024+28273*c/1048576-471*n*c/8192+9*h*c/4096)*_+(21*r/256+21*d/256+533*u/8192-21*n*u/512+197*l/4096-315*n*l/4096+584039*c/16777216-12517*n*c/131072+7*h*c/2048)*M+(151*d/6144+151*u/4096+5019*l/131072-453*n*l/16384+26965*c/786432-8607*n*c/131072)*p+(1097*u/131072+1097*l/65536+225797*c/10485760-1097*n*c/65536)*v+(8011*l/2621440+8011*c/1048576)*m+293393*c/251658240*Math.sin(12*a)}(o(d,s,t.latitude)+a*Math.cos(i),d,s);var M=r(d,t.latitude),f=r(d,c);_=Math.tan(i)*(f-M),l=h.e.negativePiToPi(t.longitude+_)}else{var p;if(c=t.latitude,0===d)p=s*Math.cos(t.latitude);else{var P=Math.sin(t.latitude);p=s*Math.cos(t.latitude)/Math.sqrt(1-g*P*P)}_=a/p,l=i>0?h.e.negativePiToPi(t.longitude+_):h.e.negativePiToPi(t.longitude-_)}return n.e(u)?(u.longitude=l,u.latitude=c,u.height=0,u):new e.a(l,c,0)}function _(t,i,a){var h=n.u(a,s.t.WGS84);this._ellipsoid=h,this._start=new e.a,this._end=new e.a,this._heading=void 0,this._distance=void 0,this._ellipticity=void 0,this._ellipticitySquared=void 0,n.e(t)&&n.e(i)&&l(this,t,i,h)}Object.defineProperties(_.prototype,{ellipsoid:{get:function(){return this._ellipsoid}},surfaceDistance:{get:function(){return a.o.defined("distance",this._distance),this._distance}},start:{get:function(){return this._start}},end:{get:function(){return this._end}},heading:{get:function(){return a.o.defined("distance",this._distance),this._heading}}}),_.fromStartHeadingDistance=function(t,i,e,o,r){a.o.defined("start",t),a.o.defined("heading",i),a.o.defined("distance",e),a.o.typeOf.number.greaterThan("distance",e,0);var d=n.u(o,s.t.WGS84),u=d.maximumRadius,l=d.minimumRadius,g=u*u,M=l*l,f=Math.sqrt((g-M)/g),p=c(t,i=h.e.negativePiToPi(i),e,d.maximumRadius,f);return!n.e(r)||n.e(o)&&!o.equals(r.ellipsoid)?new _(t,p,d):(r.setEndPoints(t,p),r)},_.prototype.setEndPoints=function(t,i){a.o.defined("start",t),a.o.defined("end",i),l(this,t,i,this._ellipsoid)},_.prototype.interpolateUsingFraction=function(t,i){return this.interpolateUsingSurfaceDistance(t*this._distance,i)},_.prototype.interpolateUsingSurfaceDistance=function(t,i){if(a.o.typeOf.number("distance",t),!n.e(this._distance)||0===this._distance)throw new a.t("EllipsoidRhumbLine must have distinct start and end set.");return c(this._start,this._heading,t,this._ellipsoid.maximumRadius,this._ellipticity,i)},_.prototype.findIntersectionWithLongitude=function(t,i){if(a.o.typeOf.number("intersectionLongitude",t),!n.e(this._distance)||0===this._distance)throw new a.t("EllipsoidRhumbLine must have distinct start and end set.");var s=this._ellipticity,o=this._heading,r=Math.abs(o),d=this._start;if(t=h.e.negativePiToPi(t),h.e.equalsEpsilon(Math.abs(t),Math.PI,h.e.EPSILON14)&&(t=h.e.sign(d.longitude)*Math.PI),n.e(i)||(i=new e.a),Math.abs(h.e.PI_OVER_TWO-r)<=h.e.EPSILON8)return i.longitude=t,i.latitude=d.latitude,i.height=0,i;if(h.e.equalsEpsilon(Math.abs(h.e.PI_OVER_TWO-r),h.e.PI_OVER_TWO,h.e.EPSILON8))return h.e.equalsEpsilon(t,d.longitude,h.e.EPSILON12)?void 0:(i.longitude=t,i.latitude=h.e.PI_OVER_TWO*h.e.sign(h.e.PI_OVER_TWO-o),i.height=0,i);var u,l=d.latitude,c=s*Math.sin(l),_=Math.tan(.5*(h.e.PI_OVER_TWO+l))*Math.exp((t-d.longitude)/Math.tan(o)),g=(1+c)/(1-c),M=d.latitude;do{u=M;var f=s*Math.sin(u),p=(1+f)/(1-f);M=2*Math.atan(_*Math.pow(p/g,s/2))-h.e.PI_OVER_TWO}while(!h.e.equalsEpsilon(M,u,h.e.EPSILON12));return i.longitude=t,i.latitude=M,i.height=0,i},_.prototype.findIntersectionWithLatitude=function(t,i){if(a.o.typeOf.number("intersectionLatitude",t),!n.e(this._distance)||0===this._distance)throw new a.t("EllipsoidRhumbLine must have distinct start and end set.");var s=this._ellipticity,o=this._heading,d=this._start;if(!h.e.equalsEpsilon(Math.abs(o),h.e.PI_OVER_TWO,h.e.EPSILON8)){var u=r(s,d.latitude),l=r(s,t),c=Math.tan(o)*(l-u),_=h.e.negativePiToPi(d.longitude+c);return n.e(i)?(i.longitude=_,i.latitude=t,i.height=0,i):new e.a(_,t,0)}},t.P=_}));
