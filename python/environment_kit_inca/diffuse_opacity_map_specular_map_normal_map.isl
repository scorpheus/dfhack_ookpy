in {
	tex2D diffuse_map;
	tex2D specular_map;
	tex2D normal_map;
	float glossiness = 0.5;
}

surface { double-sided: true, alpha-test: true }

variant {
	vertex {
		out {
			vec2 v_uv;
			vec3 v_normal;
			vec3 v_tangent;
			vec3 v_bitangent;
		}

		source %{
			v_uv = vUV0;
			v_normal = vNormal;
			v_tangent = vTangent;
			v_bitangent = vBitangent;
		%}
	}

	pixel {
		source %{
			vec3 n = texture2D(normal_map, v_uv).xyz;

			mat3 tangent_matrix = _build_mat3(normalize(v_bitangent), normalize(v_tangent), normalize(v_normal));
			n = n * 2.0 - 1.0;
			n = tangent_matrix * n;

			vec4 diffuse_color = texture2D(diffuse_map, v_uv);
			%diffuse% = diffuse_color.xyz;
			%specular% = texture2D(specular_map, v_uv).xyz;
			%normal% = n;
			%glossiness% = glossiness;
			%opacity% = diffuse_color.w;			
		%}
	}
}