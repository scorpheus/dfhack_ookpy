in {
}

surface {
	double-sided: true
}

variant {
	vertex {
        out {
            vec3 v_normal;
        }

		source %{
			%out.position% = _mtx_mul(vModelViewProjectionMatrix, vec4(vPosition, 1.0));
			v_normal = vNormal;
		%}
	}

	pixel {
		source %{
			%diffuse% = vec4(0.5,0.5,0.5,1);//vec4(v_normal, 1.0);
			//%normal% = normalize(vec3(0,1,0));
		%}
	}
}
