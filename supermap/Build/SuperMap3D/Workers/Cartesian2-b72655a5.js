define(["exports","./Cartographic-a2c313d7","./Check-52a7d806","./when-92c6cf3c","./Cartesian3-3a8bdb0b","./Math-ecf82623"],(function(e,t,r,n,o,a){"use strict";function i(e,t,i,u){t=n.u(t,0),i=n.u(i,0),u=n.u(u,0),r.o.typeOf.number.greaterThanOrEquals("x",t,0),r.o.typeOf.number.greaterThanOrEquals("y",i,0),r.o.typeOf.number.greaterThanOrEquals("z",u,0),e._radii=new o.o(t,i,u),e._radiiSquared=new o.o(t*t,i*i,u*u),e._radiiToTheFourth=new o.o(t*t*t*t,i*i*i*i,u*u*u*u),e._oneOverRadii=new o.o(0===t?0:1/t,0===i?0:1/i,0===u?0:1/u),e._oneOverRadiiSquared=new o.o(0===t?0:1/(t*t),0===i?0:1/(i*i),0===u?0:1/(u*u)),e._minimumRadius=Math.min(t,i,u),e._maximumRadius=Math.max(t,i,u),e._centerToleranceSquared=a.e.EPSILON1,0!==e._radiiSquared.z&&(e._squaredXOverSquaredZ=e._radiiSquared.x/e._radiiSquared.z)}function u(e,t,r){this._radii=void 0,this._radiiSquared=void 0,this._radiiToTheFourth=void 0,this._oneOverRadii=void 0,this._oneOverRadiiSquared=void 0,this._minimumRadius=void 0,this._maximumRadius=void 0,this._centerToleranceSquared=void 0,this._squaredXOverSquaredZ=void 0,i(this,e,t,r)}Object.defineProperties(u.prototype,{radii:{get:function(){return this._radii}},radiiSquared:{get:function(){return this._radiiSquared}},radiiToTheFourth:{get:function(){return this._radiiToTheFourth}},oneOverRadii:{get:function(){return this._oneOverRadii}},oneOverRadiiSquared:{get:function(){return this._oneOverRadiiSquared}},minimumRadius:{get:function(){return this._minimumRadius}},maximumRadius:{get:function(){return this._maximumRadius}}}),u.clone=function(e,t){if(n.e(e)){var r=e._radii;return n.e(t)?(o.o.clone(r,t._radii),o.o.clone(e._radiiSquared,t._radiiSquared),o.o.clone(e._radiiToTheFourth,t._radiiToTheFourth),o.o.clone(e._oneOverRadii,t._oneOverRadii),o.o.clone(e._oneOverRadiiSquared,t._oneOverRadiiSquared),t._minimumRadius=e._minimumRadius,t._maximumRadius=e._maximumRadius,t._centerToleranceSquared=e._centerToleranceSquared,t):new u(r.x,r.y,r.z)}},u.fromCartesian3=function(e,t){return n.e(t)||(t=new u),n.e(e)&&i(t,e.x,e.y,e.z),t},u.WGS84=Object.freeze(new u(6378137,6378137,6356752.314245179)),u.XIAN80=Object.freeze(new u(6378140,6378140,6356755.29)),u.CGCS2000=Object.freeze(new u(6378137,6378137,6356752.31)),u.UNIT_SPHERE=Object.freeze(new u(1,1,1)),u.MOON=Object.freeze(new u(a.e.LUNAR_RADIUS,a.e.LUNAR_RADIUS,a.e.LUNAR_RADIUS)),u.prototype.clone=function(e){return u.clone(this,e)},u.packedLength=o.o.packedLength,u.pack=function(e,t,a){return r.o.typeOf.object("value",e),r.o.defined("array",t),a=n.u(a,0),o.o.pack(e._radii,t,a),t},u.unpack=function(e,t,a){r.o.defined("array",e),t=n.u(t,0);var i=o.o.unpack(e,t);return u.fromCartesian3(i,a)},u.prototype.geocentricSurfaceNormal=o.o.normalize,u.prototype.geodeticSurfaceNormalCartographic=function(e,t){r.o.typeOf.object("cartographic",e);var a=e.longitude,i=e.latitude,u=Math.cos(i),s=u*Math.cos(a),c=u*Math.sin(a),h=Math.sin(i);return n.e(t)||(t=new o.o),t.x=s,t.y=c,t.z=h,o.o.normalize(t,t)},u.prototype.geodeticSurfaceNormal=function(e,t){return n.e(t)||(t=new o.o),t=o.o.multiplyComponents(e,this._oneOverRadiiSquared,t),o.o.normalize(t,t)};var s=new o.o,c=new o.o;u.prototype.cartographicToCartesian=function(e,t){var r=s,a=c;this.geodeticSurfaceNormalCartographic(e,r),o.o.multiplyComponents(this._radiiSquared,r,a);var i=Math.sqrt(o.o.dot(r,a));return o.o.divideByScalar(a,i,a),o.o.multiplyByScalar(r,e.height,r),n.e(t)||(t=new o.o),o.o.add(a,r,t)},u.prototype.cartographicArrayToCartesianArray=function(e,t){r.o.defined("cartographics",e);var o=e.length;n.e(t)?t.length=o:t=new Array(o);for(var a=0;a<o;a++)t[a]=this.cartographicToCartesian(e[a],t[a]);return t};var h=new o.o,f=new o.o,l=new o.o;function d(e,t,r,o){this.west=n.u(e,0),this.south=n.u(t,0),this.east=n.u(r,0),this.north=n.u(o,0)}u.prototype.cartesianToCartographic=function(e,r){var i=this.scaleToGeodeticSurface(e,f);if(n.e(i)){var u=this.geodeticSurfaceNormal(i,h),s=o.o.subtract(e,i,l),c=Math.atan2(u.y,u.x),d=Math.asin(u.z),p=a.e.sign(o.o.dot(s,e))*o.o.magnitude(s);return n.e(r)?(r.longitude=c,r.latitude=d,r.height=p,r):new t.a(c,d,p)}},u.prototype.cartesianArrayToCartographicArray=function(e,t){r.o.defined("cartesians",e);var o=e.length;n.e(t)?t.length=o:t=new Array(o);for(var a=0;a<o;++a)t[a]=this.cartesianToCartographic(e[a],t[a]);return t},u.prototype.scaleToGeodeticSurface=function(e,r){return t.P(e,this._oneOverRadii,this._oneOverRadiiSquared,this._centerToleranceSquared,r)},u.prototype.scaleToGeocentricSurface=function(e,t){r.o.typeOf.object("cartesian",e),n.e(t)||(t=new o.o);var a=e.x,i=e.y,u=e.z,s=this._oneOverRadiiSquared,c=1/Math.sqrt(a*a*s.x+i*i*s.y+u*u*s.z);return o.o.multiplyByScalar(e,c,t)},u.prototype.transformPositionToScaledSpace=function(e,t){return n.e(t)||(t=new o.o),o.o.multiplyComponents(e,this._oneOverRadii,t)},u.prototype.transformPositionFromScaledSpace=function(e,t){return n.e(t)||(t=new o.o),o.o.multiplyComponents(e,this._radii,t)},u.prototype.equals=function(e){return this===e||n.e(e)&&o.o.equals(this._radii,e._radii)},u.prototype.toString=function(){return this._radii.toString()},u.prototype.getSurfaceNormalIntersectionWithZAxis=function(e,t,i){if(r.o.typeOf.object("position",e),!a.e.equalsEpsilon(this._radii.x,this._radii.y,a.e.EPSILON15))throw new r.t("Ellipsoid must be an ellipsoid of revolution (radii.x == radii.y)");r.o.typeOf.number.greaterThan("Ellipsoid.radii.z",this._radii.z,0),t=n.u(t,0);var u=this._squaredXOverSquaredZ;if(n.e(i)||(i=new o.o),i.x=0,i.y=0,i.z=e.z*(1-u),!(Math.abs(i.z)>=this._radii.z-t))return i},Object.defineProperties(d.prototype,{width:{get:function(){return d.computeWidth(this)}},height:{get:function(){return d.computeHeight(this)}}}),d.packedLength=4,d.pack=function(e,t,o){return r.o.typeOf.object("value",e),r.o.defined("array",t),o=n.u(o,0),t[o++]=e.west,t[o++]=e.south,t[o++]=e.east,t[o]=e.north,t},d.unpack=function(e,t,o){return r.o.defined("array",e),t=n.u(t,0),n.e(o)||(o=new d),o.west=e[t++],o.south=e[t++],o.east=e[t++],o.north=e[t],o},d.computeWidth=function(e){r.o.typeOf.object("rectangle",e);var t=e.east,n=e.west;return t<n&&(t+=a.e.TWO_PI),t-n},d.computeHeight=function(e){return r.o.typeOf.object("rectangle",e),e.north-e.south},d.fromDegrees=function(e,t,r,o,i){return e=a.e.toRadians(n.u(e,0)),t=a.e.toRadians(n.u(t,0)),r=a.e.toRadians(n.u(r,0)),o=a.e.toRadians(n.u(o,0)),n.e(i)?(i.west=e,i.south=t,i.east=r,i.north=o,i):new d(e,t,r,o)},d.fromRadians=function(e,t,r,o,a){return n.e(a)?(a.west=n.u(e,0),a.south=n.u(t,0),a.east=n.u(r,0),a.north=n.u(o,0),a):new d(e,t,r,o)},d.fromCartographicArray=function(e,t){r.o.defined("cartographics",e);for(var o=Number.MAX_VALUE,i=-Number.MAX_VALUE,u=Number.MAX_VALUE,s=-Number.MAX_VALUE,c=Number.MAX_VALUE,h=-Number.MAX_VALUE,f=0,l=e.length;f<l;f++){var p=e[f];o=Math.min(o,p.longitude),i=Math.max(i,p.longitude),c=Math.min(c,p.latitude),h=Math.max(h,p.latitude);var y=p.longitude>=0?p.longitude:p.longitude+a.e.TWO_PI;u=Math.min(u,y),s=Math.max(s,y)}return i-o>s-u&&(o=u,(i=s)>a.e.PI&&(i-=a.e.TWO_PI),o>a.e.PI&&(o-=a.e.TWO_PI)),n.e(t)?(t.west=o,t.south=c,t.east=i,t.north=h,t):new d(o,c,i,h)},d.fromCartesianArray=function(e,t,o){r.o.defined("cartesians",e),t=n.u(t,u.WGS84);for(var i=Number.MAX_VALUE,s=-Number.MAX_VALUE,c=Number.MAX_VALUE,h=-Number.MAX_VALUE,f=Number.MAX_VALUE,l=-Number.MAX_VALUE,p=0,y=e.length;p<y;p++){var m=t.cartesianToCartographic(e[p]);i=Math.min(i,m.longitude),s=Math.max(s,m.longitude),f=Math.min(f,m.latitude),l=Math.max(l,m.latitude);var O=m.longitude>=0?m.longitude:m.longitude+a.e.TWO_PI;c=Math.min(c,O),h=Math.max(h,O)}return s-i>h-c&&(i=c,(s=h)>a.e.PI&&(s-=a.e.TWO_PI),i>a.e.PI&&(i-=a.e.TWO_PI)),n.e(o)?(o.west=i,o.south=f,o.east=s,o.north=l,o):new d(i,f,s,l)},d.clone=function(e,t){if(n.e(e))return n.e(t)?(t.west=e.west,t.south=e.south,t.east=e.east,t.north=e.north,t):new d(e.west,e.south,e.east,e.north)},d.equalsEpsilon=function(e,t,o){return r.o.typeOf.number("absoluteEpsilon",o),e===t||n.e(e)&&n.e(t)&&Math.abs(e.west-t.west)<=o&&Math.abs(e.south-t.south)<=o&&Math.abs(e.east-t.east)<=o&&Math.abs(e.north-t.north)<=o},d.prototype.clone=function(e){return d.clone(this,e)},d.prototype.equals=function(e){return d.equals(this,e)},d.equals=function(e,t){return e===t||n.e(e)&&n.e(t)&&e.west===t.west&&e.south===t.south&&e.east===t.east&&e.north===t.north},d.prototype.equalsEpsilon=function(e,t){return r.o.typeOf.number("epsilon",t),d.equalsEpsilon(this,e,t)},d.validate=function(e){r.o.typeOf.object("rectangle",e);var t=e.north;r.o.typeOf.number.greaterThanOrEquals("north",t,-a.e.PI_OVER_TWO),r.o.typeOf.number.lessThanOrEquals("north",t,a.e.PI_OVER_TWO);var n=e.south;r.o.typeOf.number.greaterThanOrEquals("south",n,-a.e.PI_OVER_TWO),r.o.typeOf.number.lessThanOrEquals("south",n,a.e.PI_OVER_TWO);var o=e.west;r.o.typeOf.number.greaterThanOrEquals("west",o,-Math.PI),r.o.typeOf.number.lessThanOrEquals("west",o,Math.PI);var i=e.east;r.o.typeOf.number.greaterThanOrEquals("east",i,-Math.PI),r.o.typeOf.number.lessThanOrEquals("east",i,Math.PI)},d.southwest=function(e,o){return r.o.typeOf.object("rectangle",e),n.e(o)?(o.longitude=e.west,o.latitude=e.south,o.height=0,o):new t.a(e.west,e.south)},d.northwest=function(e,o){return r.o.typeOf.object("rectangle",e),n.e(o)?(o.longitude=e.west,o.latitude=e.north,o.height=0,o):new t.a(e.west,e.north)},d.northeast=function(e,o){return r.o.typeOf.object("rectangle",e),n.e(o)?(o.longitude=e.east,o.latitude=e.north,o.height=0,o):new t.a(e.east,e.north)},d.southeast=function(e,o){return r.o.typeOf.object("rectangle",e),n.e(o)?(o.longitude=e.east,o.latitude=e.south,o.height=0,o):new t.a(e.east,e.south)},d.center=function(e,o){r.o.typeOf.object("rectangle",e);var i=e.east,u=e.west;i<u&&(i+=a.e.TWO_PI);var s=a.e.negativePiToPi(.5*(u+i)),c=.5*(e.south+e.north);return n.e(o)?(o.longitude=s,o.latitude=c,o.height=0,o):new t.a(s,c)},d.intersection=function(e,t,o){r.o.typeOf.object("rectangle",e),r.o.typeOf.object("otherRectangle",t);var i=e.east,u=e.west,s=t.east,c=t.west;i<u&&s>0?i+=a.e.TWO_PI:s<c&&i>0&&(s+=a.e.TWO_PI),i<u&&c<0?c+=a.e.TWO_PI:s<c&&u<0&&(u+=a.e.TWO_PI);var h=a.e.negativePiToPi(Math.max(u,c)),f=a.e.negativePiToPi(Math.min(i,s));if(!((e.west<e.east||t.west<t.east)&&f<=h)){var l=Math.max(e.south,t.south),p=Math.min(e.north,t.north);if(!(l>=p))return n.e(o)?(o.west=h,o.south=l,o.east=f,o.north=p,o):new d(h,l,f,p)}},d.simpleIntersection=function(e,t,o){r.o.typeOf.object("rectangle",e),r.o.typeOf.object("otherRectangle",t);var a=Math.max(e.west,t.west),i=Math.max(e.south,t.south),u=Math.min(e.east,t.east),s=Math.min(e.north,t.north);if(!(i>=s||a>=u))return n.e(o)?(o.west=a,o.south=i,o.east=u,o.north=s,o):new d(a,i,u,s)},d.union=function(e,t,o){r.o.typeOf.object("rectangle",e),r.o.typeOf.object("otherRectangle",t),n.e(o)||(o=new d);var i=e.east,u=e.west,s=t.east,c=t.west;i<u&&s>0?i+=a.e.TWO_PI:s<c&&i>0&&(s+=a.e.TWO_PI),i<u&&c<0?c+=a.e.TWO_PI:s<c&&u<0&&(u+=a.e.TWO_PI);var h=a.e.convertLongitudeRange(Math.min(u,c)),f=a.e.convertLongitudeRange(Math.max(i,s));return o.west=h,o.south=Math.min(e.south,t.south),o.east=f,o.north=Math.max(e.north,t.north),o},d.expand=function(e,t,o){return r.o.typeOf.object("rectangle",e),r.o.typeOf.object("cartographic",t),n.e(o)||(o=new d),o.west=Math.min(e.west,t.longitude),o.south=Math.min(e.south,t.latitude),o.east=Math.max(e.east,t.longitude),o.north=Math.max(e.north,t.latitude),o},d.contains=function(e,t){r.o.typeOf.object("rectangle",e),r.o.typeOf.object("cartographic",t);var n=t.longitude,o=t.latitude,i=e.west,u=e.east;return u<i&&(u+=a.e.TWO_PI,n<0&&(n+=a.e.TWO_PI)),(n>i||a.e.equalsEpsilon(n,i,a.e.EPSILON14))&&(n<u||a.e.equalsEpsilon(n,u,a.e.EPSILON14))&&o>=e.south&&o<=e.north};var p=new t.a;d.subsample=function(e,t,o,i){r.o.typeOf.object("rectangle",e),t=n.u(t,u.WGS84),o=n.u(o,0),n.e(i)||(i=[]);var s=0,c=e.north,h=e.south,f=e.east,l=e.west,y=p;y.height=o,y.longitude=l,y.latitude=c,i[s]=t.cartographicToCartesian(y,i[s]),s++,y.longitude=f,i[s]=t.cartographicToCartesian(y,i[s]),s++,y.latitude=h,i[s]=t.cartographicToCartesian(y,i[s]),s++,y.longitude=l,i[s]=t.cartographicToCartesian(y,i[s]),s++,y.latitude=c<0?c:h>0?h:0;for(var m=1;m<8;++m)y.longitude=-Math.PI+m*a.e.PI_OVER_TWO,d.contains(e,y)&&(i[s]=t.cartographicToCartesian(y,i[s]),s++);return 0===y.latitude&&(y.longitude=l,i[s]=t.cartographicToCartesian(y,i[s]),s++,y.longitude=f,i[s]=t.cartographicToCartesian(y,i[s]),s++),i.length=s,i};var y=new t.a;function m(e,t){this.x=n.u(e,0),this.y=n.u(t,0)}d.prototype.contains=function(e){return d.contains(this,d.southwest(e,y))&&d.contains(this,d.northwest(e,y))&&d.contains(this,d.southeast(e,y))&&d.contains(this,d.northeast(e,y))},d.MAX_VALUE=Object.freeze(new d(-Math.PI,-a.e.PI_OVER_TWO,Math.PI,a.e.PI_OVER_TWO)),m.fromElements=function(e,t,r){return n.e(r)?(r.x=e,r.y=t,r):new m(e,t)},m.clone=function(e,t){if(n.e(e))return n.e(t)?(t.x=e.x,t.y=e.y,t):new m(e.x,e.y)},m.fromCartesian3=m.clone,m.fromCartesian4=m.clone,m.packedLength=2,m.pack=function(e,t,o){return r.o.typeOf.object("value",e),r.o.defined("array",t),o=n.u(o,0),t[o++]=e.x,t[o]=e.y,t},m.unpack=function(e,t,o){return r.o.defined("array",e),t=n.u(t,0),n.e(o)||(o=new m),o.x=e[t++],o.y=e[t],o},m.packArray=function(e,t){r.o.defined("array",e);var o=e.length,a=2*o;if(n.e(t)){if(!Array.isArray(t)&&t.length!==a)throw new r.t("If result is a typed array, it must have exactly array.length * 2 elements");t.length!==a&&(t.length=a)}else t=new Array(a);for(var i=0;i<o;++i)m.pack(e[i],t,2*i);return t},m.unpackArray=function(e,t){if(r.o.defined("array",e),r.o.typeOf.number.greaterThanOrEquals("array.length",e.length,2),e.length%2!=0)throw new r.t("array length must be a multiple of 2.");var o=e.length;n.e(t)?t.length=o/2:t=new Array(o/2);for(var a=0;a<o;a+=2){var i=a/2;t[i]=m.unpack(e,a,t[i])}return t},m.fromArray=m.unpack,m.maximumComponent=function(e){return r.o.typeOf.object("cartesian",e),Math.max(e.x,e.y)},m.minimumComponent=function(e){return r.o.typeOf.object("cartesian",e),Math.min(e.x,e.y)},m.minimumByComponent=function(e,t,n){return r.o.typeOf.object("first",e),r.o.typeOf.object("second",t),r.o.typeOf.object("result",n),n.x=Math.min(e.x,t.x),n.y=Math.min(e.y,t.y),n},m.maximumByComponent=function(e,t,n){return r.o.typeOf.object("first",e),r.o.typeOf.object("second",t),r.o.typeOf.object("result",n),n.x=Math.max(e.x,t.x),n.y=Math.max(e.y,t.y),n},m.magnitudeSquared=function(e){return r.o.typeOf.object("cartesian",e),e.x*e.x+e.y*e.y},m.magnitude=function(e){return Math.sqrt(m.magnitudeSquared(e))};var O=new m;m.distance=function(e,t){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),m.subtract(e,t,O),m.magnitude(O)},m.distanceSquared=function(e,t){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),m.subtract(e,t,O),m.magnitudeSquared(O)},m.normalize=function(e,t){r.o.typeOf.object("cartesian",e),r.o.typeOf.object("result",t);var n=m.magnitude(e);if(t.x=e.x/n,t.y=e.y/n,isNaN(t.x)||isNaN(t.y))throw new r.t("normalized result is not a number");return t},m.dot=function(e,t){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),e.x*t.x+e.y*t.y},m.multiplyComponents=function(e,t,n){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),r.o.typeOf.object("result",n),n.x=e.x*t.x,n.y=e.y*t.y,n},m.divideComponents=function(e,t,n){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),r.o.typeOf.object("result",n),n.x=e.x/t.x,n.y=e.y/t.y,n},m.add=function(e,t,n){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),r.o.typeOf.object("result",n),n.x=e.x+t.x,n.y=e.y+t.y,n},m.subtract=function(e,t,n){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),r.o.typeOf.object("result",n),n.x=e.x-t.x,n.y=e.y-t.y,n},m.multiplyByScalar=function(e,t,n){return r.o.typeOf.object("cartesian",e),r.o.typeOf.number("scalar",t),r.o.typeOf.object("result",n),n.x=e.x*t,n.y=e.y*t,n},m.divideByScalar=function(e,t,n){return r.o.typeOf.object("cartesian",e),r.o.typeOf.number("scalar",t),r.o.typeOf.object("result",n),n.x=e.x/t,n.y=e.y/t,n},m.negate=function(e,t){return r.o.typeOf.object("cartesian",e),r.o.typeOf.object("result",t),t.x=-e.x,t.y=-e.y,t},m.abs=function(e,t){return r.o.typeOf.object("cartesian",e),r.o.typeOf.object("result",t),t.x=Math.abs(e.x),t.y=Math.abs(e.y),t};var g=new m;m.lerp=function(e,t,n,o){return r.o.typeOf.object("start",e),r.o.typeOf.object("end",t),r.o.typeOf.number("t",n),r.o.typeOf.object("result",o),m.multiplyByScalar(t,n,g),o=m.multiplyByScalar(e,1-n,o),m.add(g,o,o)};var b=new m,_=new m;m.angleBetween=function(e,t){return r.o.typeOf.object("left",e),r.o.typeOf.object("right",t),m.normalize(e,b),m.normalize(t,_),a.e.acosClamped(m.dot(b,_))};var w=new m;m.mostOrthogonalAxis=function(e,t){r.o.typeOf.object("cartesian",e),r.o.typeOf.object("result",t);var n=m.normalize(e,w);return m.abs(n,n),t=n.x<=n.y?m.clone(m.UNIT_X,t):m.clone(m.UNIT_Y,t)},m.equals=function(e,t){return e===t||n.e(e)&&n.e(t)&&e.x===t.x&&e.y===t.y},m.equalsArray=function(e,t,r){return e.x===t[r]&&e.y===t[r+1]},m.equalsEpsilon=function(e,t,r,o){return e===t||n.e(e)&&n.e(t)&&a.e.equalsEpsilon(e.x,t.x,r,o)&&a.e.equalsEpsilon(e.y,t.y,r,o)},m.ZERO=Object.freeze(new m(0,0)),m.UNIT_X=Object.freeze(new m(1,0)),m.UNIT_Y=Object.freeze(new m(0,1)),m.prototype.clone=function(e){return m.clone(this,e)},m.prototype.equals=function(e){return m.equals(this,e)},m.prototype.equalsEpsilon=function(e,t,r){return m.equalsEpsilon(this,e,t,r)},m.prototype.toString=function(){return"("+this.x+", "+this.y+")"},m.prototype.toArray=function(e,t){m.pack(this,e,t)},e.h=d,e.o=m,e.t=u}));
