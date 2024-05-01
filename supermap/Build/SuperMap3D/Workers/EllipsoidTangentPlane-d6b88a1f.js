define(["exports","./Cartesian3-3a8bdb0b","./Check-52a7d806","./when-92c6cf3c","./buildModuleUrl-9eef8841","./Cartesian2-b72655a5","./Cartesian4-72b88c9e","./IntersectionTests-6e80d61c","./FeatureDetection-cec0163f","./Plane-33393da8","./GeometryAttribute-f47bd1cb"],(function(e,t,n,i,o,r,a,s,c,m,u){"use strict";function l(e,n,o){this.minimum=t.o.clone(i.u(e,t.o.ZERO)),this.maximum=t.o.clone(i.u(n,t.o.ZERO)),o=i.e(o)?t.o.clone(o):t.o.midpoint(this.minimum,this.maximum,new t.o),this.center=o}l.fromPoints=function(e,n){if(i.e(n)||(n=new l),!i.e(e)||0===e.length)return n.minimum=t.o.clone(t.o.ZERO,n.minimum),n.maximum=t.o.clone(t.o.ZERO,n.maximum),n.center=t.o.clone(t.o.ZERO,n.center),n;for(var o=e[0].x,r=e[0].y,a=e[0].z,s=e[0].x,c=e[0].y,m=e[0].z,u=e.length,h=1;h<u;h++){var f=e[h],p=f.x,d=f.y,x=f.z;o=Math.min(p,o),s=Math.max(p,s),r=Math.min(d,r),c=Math.max(d,c),a=Math.min(x,a),m=Math.max(x,m)}var y=n.minimum;y.x=o,y.y=r,y.z=a;var g=n.maximum;return g.x=s,g.y=c,g.z=m,n.center=t.o.midpoint(y,g,n.center),n},l.clone=function(e,n){if(i.e(e))return i.e(n)?(n.minimum=t.o.clone(e.minimum,n.minimum),n.maximum=t.o.clone(e.maximum,n.maximum),n.center=t.o.clone(e.center,n.center),n):new l(e.minimum,e.maximum,e.center)},l.equals=function(e,n){return e===n||i.e(e)&&i.e(n)&&t.o.equals(e.center,n.center)&&t.o.equals(e.minimum,n.minimum)&&t.o.equals(e.maximum,n.maximum)};var h=new t.o;l.intersectPlane=function(e,i){n.o.defined("box",e),n.o.defined("plane",i),h=t.o.subtract(e.maximum,e.minimum,h);var r=t.o.multiplyByScalar(h,.5,h),a=i.normal,s=r.x*Math.abs(a.x)+r.y*Math.abs(a.y)+r.z*Math.abs(a.z),c=t.o.dot(e.center,a)+i.distance;return c-s>0?o.S.INSIDE:c+s<0?o.S.OUTSIDE:o.S.INTERSECTING},l.prototype.clone=function(e){return l.clone(this,e)},l.prototype.intersectPlane=function(e){return l.intersectPlane(this,e)},l.prototype.equals=function(e){return l.equals(this,e)};var f=new a.e;function p(e,o){if(n.o.defined("origin",e),e=(o=i.u(o,r.t.WGS84)).scaleToGeodeticSurface(e),!i.e(e))throw new n.t("origin must not be at the center of the ellipsoid.");var a=u.m.eastNorthUpToFixedFrame(e,o);this._ellipsoid=o,this._origin=e,this._xAxis=t.o.fromCartesian4(c.p.getColumn(a,0,f)),this._yAxis=t.o.fromCartesian4(c.p.getColumn(a,1,f));var s=t.o.fromCartesian4(c.p.getColumn(a,2,f));this._plane=m.o.fromPointNormal(e,s)}Object.defineProperties(p.prototype,{ellipsoid:{get:function(){return this._ellipsoid}},origin:{get:function(){return this._origin}},plane:{get:function(){return this._plane}},xAxis:{get:function(){return this._xAxis}},yAxis:{get:function(){return this._yAxis}},zAxis:{get:function(){return this._plane.normal}}});var d=new l;p.fromPoints=function(e,t){return n.o.defined("cartesians",e),new p(l.fromPoints(e,d).center,t)};var x=new s.f,y=new t.o;p.prototype.projectPointOntoPlane=function(e,o){n.o.defined("cartesian",e);var a=x;a.origin=e,t.o.normalize(e,a.direction);var c=s.g.rayPlane(a,this._plane,y);if(i.e(c)||(t.o.negate(a.direction,a.direction),c=s.g.rayPlane(a,this._plane,y)),i.e(c)){var m=t.o.subtract(c,this._origin,c),u=t.o.dot(this._xAxis,m),l=t.o.dot(this._yAxis,m);return i.e(o)?(o.x=u,o.y=l,o):new r.o(u,l)}},p.prototype.projectPointsOntoPlane=function(e,t){n.o.defined("cartesians",e),i.e(t)||(t=[]);for(var o=0,r=e.length,a=0;a<r;a++){var s=this.projectPointOntoPlane(e[a],t[o]);i.e(s)&&(t[o]=s,o++)}return t.length=o,t},p.prototype.projectPointToNearestOnPlane=function(e,o){n.o.defined("cartesian",e),i.e(o)||(o=new r.o);var a=x;a.origin=e,t.o.clone(this._plane.normal,a.direction);var c=s.g.rayPlane(a,this._plane,y);i.e(c)||(t.o.negate(a.direction,a.direction),c=s.g.rayPlane(a,this._plane,y));var m=t.o.subtract(c,this._origin,c),u=t.o.dot(this._xAxis,m),l=t.o.dot(this._yAxis,m);return o.x=u,o.y=l,o},p.prototype.projectPointsToNearestOnPlane=function(e,t){n.o.defined("cartesians",e),i.e(t)||(t=[]);var o=e.length;t.length=o;for(var r=0;r<o;r++)t[r]=this.projectPointToNearestOnPlane(e[r],t[r]);return t};var g=new t.o;p.prototype.projectPointOntoEllipsoid=function(e,o){n.o.defined("cartesian",e),i.e(o)||(o=new t.o);var r=this._ellipsoid,a=this._origin,s=this._xAxis,c=this._yAxis,m=g;return t.o.multiplyByScalar(s,e.x,m),o=t.o.add(a,m,o),t.o.multiplyByScalar(c,e.y,m),t.o.add(o,m,o),r.scaleToGeocentricSurface(o,o),o},p.prototype.projectPointsOntoEllipsoid=function(e,t){n.o.defined("cartesians",e);var o=e.length;i.e(t)?t.length=o:t=new Array(o);for(var r=0;r<o;++r)t[r]=this.projectPointOntoEllipsoid(e[r],t[r]);return t},e.e=l,e.f=p}));
