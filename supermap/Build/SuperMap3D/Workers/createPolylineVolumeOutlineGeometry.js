define(["./when-92c6cf3c","./Cartesian2-b72655a5","./arrayRemoveDuplicates-a6924649","./BoundingRectangle-82c0e2a7","./buildModuleUrl-9eef8841","./Cartesian3-3a8bdb0b","./ComponentDatatype-98414d16","./PolylineVolumeGeometryLibrary-d96626d0","./Check-52a7d806","./GeometryAttribute-f47bd1cb","./GeometryAttributes-7f66ea53","./IndexDatatype-86677ec4","./Math-ecf82623","./PolygonPipeline-425528b3","./FeatureDetection-cec0163f","./Cartographic-a2c313d7","./Event-3390cd7d","./RuntimeError-c6a62a80","./WebGLConstants-42651efd","./Cartesian4-72b88c9e","./EllipsoidTangentPlane-d6b88a1f","./IntersectionTests-6e80d61c","./Plane-33393da8","./PolylinePipeline-f0970409","./EllipsoidGeodesic-03c935a0","./EllipsoidRhumbLine-b1a766ae"],(function(e,t,i,n,o,r,a,s,p,l,c,u,d,h,y,f,g,v,_,m,P,k,b,w,E,D){"use strict";function L(i){var n=(i=e.u(i,e.u.EMPTY_OBJECT)).polylinePositions,o=i.shapePositions;if(!e.e(n))throw new p.t("options.polylinePositions is required.");if(!e.e(o))throw new p.t("options.shapePositions is required.");this._positions=n,this._shape=o,this._ellipsoid=t.t.clone(e.u(i.ellipsoid,t.t.WGS84)),this._cornerType=e.u(i.cornerType,s.S.ROUNDED),this._granularity=e.u(i.granularity,d.e.RADIANS_PER_DEGREE),this._workerName="createPolylineVolumeOutlineGeometry";var a=1+n.length*r.o.packedLength;a+=1+o.length*t.o.packedLength,this.packedLength=a+t.t.packedLength+2}L.pack=function(i,n,o){if(!e.e(i))throw new p.t("value is required");if(!e.e(n))throw new p.t("array is required");o=e.u(o,0);var a,s=i._positions,l=s.length;for(n[o++]=l,a=0;a<l;++a,o+=r.o.packedLength)r.o.pack(s[a],n,o);var c=i._shape;for(l=c.length,n[o++]=l,a=0;a<l;++a,o+=t.o.packedLength)t.o.pack(c[a],n,o);return t.t.pack(i._ellipsoid,n,o),o+=t.t.packedLength,n[o++]=i._cornerType,n[o]=i._granularity,n};var T=t.t.clone(t.t.UNIT_SPHERE),C={polylinePositions:void 0,shapePositions:void 0,ellipsoid:T,height:void 0,cornerType:void 0,granularity:void 0};L.unpack=function(i,n,o){if(!e.e(i))throw new p.t("array is required");n=e.u(n,0);var a,s=i[n++],l=new Array(s);for(a=0;a<s;++a,n+=r.o.packedLength)l[a]=r.o.unpack(i,n);s=i[n++];var c=new Array(s);for(a=0;a<s;++a,n+=t.o.packedLength)c[a]=t.o.unpack(i,n);var u=t.t.unpack(i,n,T);n+=t.t.packedLength;var d=i[n++],h=i[n];return e.e(o)?(o._positions=l,o._shape=c,o._ellipsoid=t.t.clone(u,o._ellipsoid),o._cornerType=d,o._granularity=h,o):(C.polylinePositions=l,C.shapePositions=c,C.cornerType=d,C.granularity=h,new L(C))};var A=new n.f;return L.createGeometry=function(e){var t=e._positions,p=i.D(t,r.o.equalsEpsilon),d=e._shape;if(d=s.J.removeDuplicatesFromShape(d),!(p.length<2||d.length<3)){h.A.computeWindingOrder2D(d)===h.W.CLOCKWISE&&d.reverse();var f=n.f.fromPoints(d,A);return function(e,t){var i=new c.a;i.position=new l.o({componentDatatype:a.ComponentDatatype.DOUBLE,componentsPerAttribute:3,values:e});var n,r,s=t.length,p=i.position.values.length/3,d=e.length/3/s,h=u.IndexDatatype.createTypedArray(p,2*s*(d+1)),f=0,g=(n=0)*s;for(r=0;r<s-1;r++)h[f++]=r+g,h[f++]=r+g+1;for(h[f++]=s-1+g,h[f++]=g,g=(n=d-1)*s,r=0;r<s-1;r++)h[f++]=r+g,h[f++]=r+g+1;for(h[f++]=s-1+g,h[f++]=g,n=0;n<d-1;n++){var v=s*n,_=v+s;for(r=0;r<s;r++)h[f++]=r+v,h[f++]=r+_}return new l.I({attributes:i,indices:u.IndexDatatype.createTypedArray(p,h),boundingSphere:o.i.fromVertices(e),primitiveType:y._0x4b6a27.LINES})}(s.J.computePositions(p,d,f,e,!1),d)}},function(i,n){return e.e(n)&&(i=L.unpack(i,n)),i._ellipsoid=t.t.clone(i._ellipsoid),L.createGeometry(i)}}));
