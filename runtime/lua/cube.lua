-- %{Name=Cube;Type=SceneCreate;Menu=Primitive%}
execution_context = gs.ScriptContextAll

width = 1 --> float
height = 1 --> float
length = 1 --> float

function CreateRenderGeometry(uname)
	geo = gs.CoreGeometry()
	geo:SetName(uname)

	d = gs.Vector3(width, height, length)
	d = d * 0.5

	geo:AllocateMaterialTable(1)
	geo:SetMaterial(0, "@core/materials/default.xml", true)

	-- generate vertices
	if geo:AllocateVertex(8) == 0 then
		return
	end

	geo:SetVertex(0,-d.x, d.y, d.z);
	geo:SetVertex(1, d.x, d.y, d.z);
	geo:SetVertex(2, d.x, d.y, -d.z);
	geo:SetVertex(3,-d.x, d.y, -d.z);
	geo:SetVertex(4,-d.x, -d.y, d.z);
	geo:SetVertex(5, d.x, -d.y, d.z);
	geo:SetVertex(6, d.x, -d.y, -d.z);
	geo:SetVertex(7,-d.x, -d.y, -d.z);

	-- build polygons
	if geo:AllocatePolygon(6) == 0 then
		return
	end

	for n=0,6 do
	   geo:SetPolygon(n, 4, 0)
	end

    geo:AllocateRgb(6*4)
    geo:AllocateUVChannel(3, 6*4)

	if geo:AllocatePolygonBinding() == 0 then
		return
	end

	geo:SetPolygonBinding(0, {0,1,2,3})
	geo:SetPolygonBinding(1, {3,2,6,7})
	geo:SetPolygonBinding(2, {7,6,5,4})
	geo:SetPolygonBinding(3, {4,5,1,0})
	geo:SetPolygonBinding(4, {2,1,5,6})
	geo:SetPolygonBinding(5, {0,3,7,4})

    for c=0,5 do
        geo:SetRgb(c, {gs.Color.One, gs.Color.One, gs.Color.One})
    end

    geo:SetUV(0, 0, {gs.Vector2(0.5, 0), gs.Vector2(0.5, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0)})
    geo:SetUV(0, 1, {gs.Vector2(0, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0.66), gs.Vector2(0, 0.66)})
    geo:SetUV(0, 2, {gs.Vector2(0.25, 1), gs.Vector2(0.25, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 1)})
    geo:SetUV(0, 3, {gs.Vector2(0.75, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 0.33), gs.Vector2(0.75, 0.33)})
    geo:SetUV(0, 4, {gs.Vector2(0.25, 0.33), gs.Vector2(0.5, 0.33), gs.Vector2(0.5, 0.66), gs.Vector2(0.25, 0.66)})
    geo:SetUV(0, 5, {gs.Vector2(0.75, 0.33), gs.Vector2(1, 0.33), gs.Vector2(1, 0.66), gs.Vector2(0.75, 0.66)})

    geo:SetUV(1, 0, {gs.Vector2(0.5, 0), gs.Vector2(0.5, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0)})
    geo:SetUV(1, 1, {gs.Vector2(0, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0.66), gs.Vector2(0, 0.66)})
    geo:SetUV(1, 2, {gs.Vector2(0.25, 1), gs.Vector2(0.25, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 1)})
    geo:SetUV(1, 3, {gs.Vector2(0.75, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 0.33), gs.Vector2(0.75, 0.33)})
    geo:SetUV(1, 4, {gs.Vector2(0.25, 0.33), gs.Vector2(0.5, 0.33), gs.Vector2(0.5, 0.66), gs.Vector2(0.25, 0.66)})
    geo:SetUV(1, 5, {gs.Vector2(0.75, 0.33), gs.Vector2(1, 0.33), gs.Vector2(1, 0.66), gs.Vector2(0.75, 0.66)})

    geo:SetUV(2, 0, {gs.Vector2(0.5, 0), gs.Vector2(0.5, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0)})
    geo:SetUV(2, 1, {gs.Vector2(0, 0.33), gs.Vector2(0.25, 0.33), gs.Vector2(0.25, 0.66), gs.Vector2(0, 0.66)})
    geo:SetUV(2, 2, {gs.Vector2(0.25, 1), gs.Vector2(0.25, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 1)})
    geo:SetUV(2, 3, {gs.Vector2(0.75, 0.66), gs.Vector2(0.5, 0.66), gs.Vector2(0.5, 0.33), gs.Vector2(0.75, 0.33)})
    geo:SetUV(2, 4, {gs.Vector2(0.25, 0.33), gs.Vector2(0.5, 0.33), gs.Vector2(0.5, 0.66), gs.Vector2(0.25, 0.66)})
    geo:SetUV(2, 5, {gs.Vector2(0.75, 0.33), gs.Vector2(1, 0.33), gs.Vector2(1, 0.66), gs.Vector2(0.75, 0.66)})

	geo:ComputeVertexNormal(0.7)
    geo:ComputeVertexTangent()

	return render_system:CreateGeometry(geo)
end

function GetUniqueName()
	return "@gen/cube_"..width.."_"..height.."_"..length
end

function Setup()
	render_system = engine:GetRenderSystemAsync()

	uname = GetUniqueName()
	render_geo = render_system:HasGeometry(uname)

	if render_geo == nil then
		render_geo = CreateRenderGeometry(uname)
	end

	if object == nil then
		if this.object == nil then
			object = gs.Object()
			this:AddComponent(object)
		else
			object = this.object
		end
	end

	object:SetDoNotSerialize(true)
	object:SetGeometry(render_geo)
end

function OnEditorSetParameter(name)
	Setup() -- simply regenerate the geometry on parameter change
end

function Delete()
	this:RemoveComponent(object)
end
