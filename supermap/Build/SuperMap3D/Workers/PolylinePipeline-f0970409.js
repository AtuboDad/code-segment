define(["exports","./Cartesian3-3a8bdb0b","./Cartographic-a2c313d7","./when-92c6cf3c","./Check-52a7d806","./Cartesian2-b72655a5","./EllipsoidGeodesic-03c935a0","./EllipsoidRhumbLine-b1a766ae","./IntersectionTests-6e80d61c","./Math-ecf82623","./FeatureDetection-cec0163f","./Plane-33393da8"],(function(e,r,a,t,n,o,i,c,s,u,h,l){"use strict";var f={numberOfPoints:function(e,a,t){var n=r.o.distance(e,a);return Math.ceil(n/t)},numberOfPointsRhumbLine:function(e,r,a){var t=Math.pow(e.longitude-r.longitude,2)+Math.pow(e.latitude-r.latitude,2);return Math.ceil(Math.sqrt(t/(a*a)))}},g=new a.a;f.extractHeights=function(e,r){for(var a=e.length,t=new Array(a),n=0;n<a;n++){var o=e[n];t[n]=r.cartesianToCartographic(o,g).height}return t};var p=new h.p,v=new r.o,d=new r.o,m=new l.o(r.o.UNIT_X,0),w=new r.o,T=new l.o(r.o.UNIT_X,0),y=new r.o,P=new r.o,A=[];function C(e,r,a){var t,n=A;if(n.length=e,r===a){for(t=0;t<e;t++)n[t]=r;return n}var o=(a-r)/e;for(t=0;t<e;t++){var i=r+t*o;n[t]=i}return n}var b=new a.a,S=new a.a,E=new r.o,R=new r.o,D=new r.o,G=new i.E,N=new c.P;function I(e,a,t,n,o,i,c,s,u){var h=n.scaleToGeodeticSurface(e,R),l=n.scaleToGeodeticSurface(a,D),g=f.numberOfPoints(e,a,t),p=n.cartesianToCartographic(h,b),v=n.cartesianToCartographic(l,S),d=C(g,o,i);u>0&&(d=function(e,r){var a=A;a.length=e;for(var t=0;t<e;t++)a[t]+=r*Math.sin(Math.PI*t/e);return a}(g,u)),G.setEndPoints(p,v);var m=G.surfaceDistance/g,w=s;p.height=o;var T=n.cartographicToCartesian(p,E);r.o.pack(T,c,w),w+=3;for(var y=1;y<g;y++){var P=G.interpolateUsingSurfaceDistance(y*m,S);P.height=d[y],T=n.cartographicToCartesian(P,E),r.o.pack(T,c,w),w+=3}return w}function k(e,a,t,n,o,i,s,u){var h=n.scaleToGeodeticSurface(e,R),l=n.scaleToGeodeticSurface(a,D),g=n.cartesianToCartographic(h,b),p=n.cartesianToCartographic(l,S),v=f.numberOfPointsRhumbLine(g,p,t),d=C(v,o,i);N.ellipsoid.equals(n)||(N=new c.P(void 0,void 0,n)),N.setEndPoints(g,p);var m=N.surfaceDistance/v,w=u;g.height=o;var T=n.cartographicToCartesian(g,E);r.o.pack(T,s,w),w+=3;for(var y=1;y<v;y++){var P=N.interpolateUsingSurfaceDistance(y*m,S);P.height=d[y],T=n.cartographicToCartesian(P,E),r.o.pack(T,s,w),w+=3}return w}f.wrapLongitude=function(e,a){var n=[],o=[];if(t.e(e)&&e.length>0){a=t.u(a,h.p.IDENTITY);var i=h.p.inverseTransformation(a,p),c=h.p.multiplyByPoint(i,r.o.ZERO,v),u=r.o.normalize(h.p.multiplyByPointAsVector(i,r.o.UNIT_Y,d),d),f=l.o.fromPointNormal(c,u,m),g=r.o.normalize(h.p.multiplyByPointAsVector(i,r.o.UNIT_X,w),w),A=l.o.fromPointNormal(c,g,T),C=1;n.push(r.o.clone(e[0]));for(var b=n[0],S=e.length,E=1;E<S;++E){var R=e[E];if(l.o.getPointDistance(A,b)<0||l.o.getPointDistance(A,R)<0){var D=s.g.lineSegmentPlane(b,R,f,y);if(t.e(D)){var G=r.o.multiplyByScalar(u,5e-9,P);l.o.getPointDistance(f,b)<0&&r.o.negate(G,G),n.push(r.o.add(D,G,new r.o)),o.push(C+1),r.o.negate(G,G),n.push(r.o.add(D,G,new r.o)),C=1}}n.push(r.o.clone(e[E])),C++,b=R}o.push(C)}return{positions:n,lengths:o}},f.generateArc=function(e){t.e(e)||(e={});var a=e.positions;if(!t.e(a))throw new n.t("options.positions is required.");var i=a.length,c=t.u(e.ellipsoid,o.t.WGS84),s=t.u(e.height,0),h=Array.isArray(s);if(i<1)return[];if(1===i){var l=c.scaleToGeodeticSurface(a[0],R);if(0!==(s=h?s[0]:s)){var g=c.geodeticSurfaceNormal(l,E);r.o.multiplyByScalar(g,s,g),r.o.add(l,g,l)}return[l.x,l.y,l.z]}var p=e.minDistance;if(!t.e(p)){var v=t.u(e.granularity,u.e.RADIANS_PER_DEGREE);p=u.e.chordLength(v,c.maximumRadius)}var d,m=0;for(d=0;d<i-1;d++)m+=f.numberOfPoints(a[d],a[d+1],p);var w=e.hMax,T=3*(m+1),y=new Array(T),P=0;for(d=0;d<i-1;d++){P=I(a[d],a[d+1],p,c,h?s[d]:s,h?s[d+1]:s,y,P,w)}A.length=0;var C=a[i-1],S=c.cartesianToCartographic(C,b);S.height=h?s[i-1]:s;var D=c.cartographicToCartesian(S,E);return r.o.pack(D,y,T-3),y};var M=new a.a,_=new a.a;f.generateRhumbArc=function(e){t.e(e)||(e={});var i=e.positions;if(!t.e(i))throw new n.t("options.positions is required.");var c=i.length,s=t.u(e.ellipsoid,o.t.WGS84),h=t.u(e.height,0),l=Array.isArray(h);if(c<1)return[];if(1===c){var g=s.scaleToGeodeticSurface(i[0],R);if(0!==(h=l?h[0]:h)){var p=s.geodeticSurfaceNormal(g,E);r.o.multiplyByScalar(p,h,p),r.o.add(g,p,g)}return[g.x,g.y,g.z]}var v,d,m=t.u(e.granularity,u.e.RADIANS_PER_DEGREE),w=0,T=s.cartesianToCartographic(i[0],M);for(v=0;v<c-1;v++)d=s.cartesianToCartographic(i[v+1],_),w+=f.numberOfPointsRhumbLine(T,d,m),T=a.a.clone(d,M);var y=3*(w+1),P=new Array(y),C=0;for(v=0;v<c-1;v++){C=k(i[v],i[v+1],m,s,l?h[v]:h,l?h[v+1]:h,P,C)}A.length=0;var S=i[c-1],D=s.cartesianToCartographic(S,b);D.height=l?h[c-1]:h;var G=s.cartographicToCartesian(D,E);return r.o.pack(G,P,y-3),P},f.generateCartesianArc=function(e){for(var a=f.generateArc(e),t=a.length/3,n=new Array(t),o=0;o<t;o++)n[o]=r.o.unpack(a,3*o);return n},f.generateCartesianRhumbArc=function(e){for(var a=f.generateRhumbArc(e),t=a.length/3,n=new Array(t),o=0;o<t;o++)n[o]=r.o.unpack(a,3*o);return n},e.m=f}));
