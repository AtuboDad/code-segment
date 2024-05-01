define(["./when-92c6cf3c","./buildModuleUrl-9eef8841","./Cartesian3-3a8bdb0b","./Check-52a7d806","./ComponentDatatype-98414d16","./FrustumGeometry-9ce10b65","./GeometryAttribute-f47bd1cb","./GeometryAttributes-7f66ea53","./FeatureDetection-cec0163f","./Cartographic-a2c313d7","./Math-ecf82623","./Cartesian2-b72655a5","./Event-3390cd7d","./RuntimeError-c6a62a80","./WebGLConstants-42651efd","./Cartesian4-72b88c9e","./Plane-33393da8","./VertexFormat-f496a3f1"],(function(e,t,n,a,r,o,i,c,u,p,s,f,d,m,_,k,h,g){"use strict";function y(t){a.o.typeOf.object("options",t),a.o.typeOf.object("options.frustum",t.frustum),a.o.typeOf.object("options.origin",t.origin),a.o.typeOf.object("options.orientation",t.orientation);var r,c,u=t.frustum,p=t.orientation,s=t.origin,f=e.u(t._drawNearPlane,!0);u instanceof o.o?(r=0,c=o.o.packedLength):u instanceof o.a&&(r=1,c=o.a.packedLength),this._frustumType=r,this._frustum=u.clone(),this._origin=n.o.clone(s),this._orientation=i.n.clone(p),this._drawNearPlane=f,this._workerName="createFrustumOutlineGeometry",this.packedLength=2+c+n.o.packedLength+i.n.packedLength}y.pack=function(t,r,c){a.o.typeOf.object("value",t),a.o.defined("array",r),c=e.u(c,0);var u=t._frustumType,p=t._frustum;return r[c++]=u,0===u?(o.o.pack(p,r,c),c+=o.o.packedLength):(o.a.pack(p,r,c),c+=o.a.packedLength),n.o.pack(t._origin,r,c),c+=n.o.packedLength,i.n.pack(t._orientation,r,c),r[c+=i.n.packedLength]=t._drawNearPlane?1:0,r};var b=new o.o,l=new o.a,w=new i.n,L=new n.o;return y.unpack=function(t,r,c){a.o.defined("array",t),r=e.u(r,0);var u,p=t[r++];0===p?(u=o.o.unpack(t,r,b),r+=o.o.packedLength):(u=o.a.unpack(t,r,l),r+=o.a.packedLength);var s=n.o.unpack(t,r,L);r+=n.o.packedLength;var f=i.n.unpack(t,r,w),d=1===t[r+=i.n.packedLength];if(!e.e(c))return new y({frustum:u,origin:s,orientation:f,_drawNearPlane:d});var m=p===c._frustumType?c._frustum:void 0;return c._frustum=u.clone(m),c._frustumType=p,c._origin=n.o.clone(s,c._origin),c._orientation=i.n.clone(f,c._orientation),c._drawNearPlane=d,c},y.createGeometry=function(e){var n=e._frustumType,a=e._frustum,p=e._origin,s=e._orientation,f=e._drawNearPlane,d=new Float64Array(24);o.z._computeNearFarPlanes(p,s,n,a,d);for(var m,_,k=new c.a({position:new i.o({componentDatatype:r.ComponentDatatype.DOUBLE,componentsPerAttribute:3,values:d})}),h=f?2:1,g=new Uint16Array(8*(h+1)),y=f?0:1;y<2;++y)_=4*y,g[m=f?8*y:0]=_,g[m+1]=_+1,g[m+2]=_+1,g[m+3]=_+2,g[m+4]=_+2,g[m+5]=_+3,g[m+6]=_+3,g[m+7]=_;for(y=0;y<2;++y)_=4*y,g[m=8*(h+y)]=_,g[m+1]=_+4,g[m+2]=_+1,g[m+3]=_+5,g[m+4]=_+2,g[m+5]=_+6,g[m+6]=_+3,g[m+7]=_+7;return new i.I({attributes:k,indices:g,primitiveType:u._0x4b6a27.LINES,boundingSphere:t.i.fromVertices(d)})},function(t,n){return e.e(n)&&(t=y.unpack(t,n)),y.createGeometry(t)}}));
