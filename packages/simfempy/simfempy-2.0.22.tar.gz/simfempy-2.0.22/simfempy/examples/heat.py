assert __name__ == '__main__'
# in shell
import os, sys
simfempypath = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir,'simfempy'))
sys.path.insert(0,simfempypath)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pygmsh
from simfempy.applications.heat import Heat
from simfempy.applications.problemdata import ProblemData
from simfempy.meshes.simplexmesh import SimplexMesh
from simfempy.meshes import plotmesh, animdata

# ---------------------------------------------------------------- #
def main(mode = 'static', h=0.1, convection=True, fem='p1', plot='data'):
    #create mesh
    mesh = createMesh(h=h)
    if plot=='numbering':
        from simfempy.meshes.plotmesh import plotmeshWithNumbering
        plotmeshWithNumbering(mesh)
        return
    if plot=='boundary':
        plotmesh.meshWithBoundaries(mesh)
        return
    #create problem data
    problemdata = createProblemData(mode, convection=convection)
    #create application
    heat = Heat(mesh=mesh, problemdata=problemdata, fem='p1')
    if mode == 'static':
        result = heat.static()
        print(f"{result.info['timer']}")
        print(f"postproc:")
        for p,v in result.data['global'].items(): print(f"{p}: {v}")
        fig = plt.figure(figsize=(10, 8))
        fig.suptitle("Heat static", fontsize=16)
        outer = gridspec.GridSpec(1, 2, wspace=0.2, hspace=0.2)
        plotmesh.meshWithBoundaries(heat.mesh, fig=fig, outer=outer[0])
        plotmesh.meshWithData(heat.mesh, data=result.data, alpha=0.1,fig=fig, outer=outer[1])
        nodes = np.unique(heat.mesh.linesoflabel[999])
        nodes2 = np.unique(heat.mesh.linesoflabel[1002])
        u = result.data['point']['U']
        ax = fig.gca()
        ins = ax.inset_axes([0.6, 0.6, 0.4, 0.4])
        ins.plot(heat.mesh.points[nodes,0], u[nodes], 'xr')
        ins.set_title("999")
        ins = ax.inset_axes([0, 0, 0.4, 0.4])
        ins.plot(heat.mesh.points[nodes2,0], u[nodes2], 'xb')
        ins.set_title("1002", color='w')
        plt.show()
    elif mode == 'dynamic':
        u0 = heat.initialCondition()
        t_final, dt = 2000, 10
        nframes = int(t_final/dt/4)
        result = heat.dynamic(u0, t_span=(0,t_final), nframes=nframes, dt=dt, method='BE')
        u = result.data['point']['U']
        fig = plt.figure(figsize=(10, 8))
        outer = gridspec.GridSpec(1, 3, wspace=0.2, hspace=0.2)
        plotmesh.meshWithData(heat.mesh, point_data={'u0':u0}, fig=fig, outer=outer[0])
        plotmesh.meshWithData(heat.mesh, point_data={'u1':u[0]}, fig=fig, outer=outer[1])
        plotmesh.meshWithData(heat.mesh, point_data={'uN':u[-1]}, fig=fig, outer=outer[2])
        anim = animdata.AnimData(mesh, u)
        plt.show()
    else: raise ValueError(f"unknown{ mode=}")

# ---------------------------------------------------------------- #
def createMesh(h=0.2):
    with pygmsh.geo.Geometry() as geom:
        holes = []
        rectangle = geom.add_rectangle(xmin=-1.5, xmax=-0.5, ymin=-1.5, ymax=-0.5, z=0, mesh_size=h)
        geom.add_physical(rectangle.surface, label="200")
        geom.add_physical(rectangle.lines, label="20") #required for correct boundary labels (!?)
        holes.append(rectangle)
        circle = geom.add_circle(x0=[0,0], radius=0.5, mesh_size=h, num_sections=6, make_surface=False)
        geom.add_physical(circle.curve_loop.curves, label="3000")
        holes.append(circle)
        p = geom.add_rectangle(xmin=-2, xmax=2, ymin=-2, ymax=2, z=0, mesh_size=h, holes=holes)
        geom.add_physical(p.surface, label="100")
        for i in range(len(p.lines)): geom.add_physical(p.lines[i], label=f"{1000 + i}")

        p1 = geom.add_point((-1., 1.5, 0.), mesh_size=0.1*h)
        p2 = geom.add_point(( 1., 1.5, 0.), mesh_size=0.2*h)
        l6 = geom.add_line(p1, p2)
        geom.add_physical(p1, label="9999")
        geom.in_surface(l6, p.surface)
        geom.add_physical(l6, label="999")

        mesh = geom.generate_mesh()
    return SimplexMesh(mesh=mesh)
# ---------------------------------------------------------------- #
def createProblemData(mode='static', convection=False):
    data = ProblemData()
    #boundary conditions
    data.bdrycond.set("Dirichlet", [1000, 3000])
    data.bdrycond.set("Neumann", [1001, 1002, 1003])
    data.bdrycond.fct[1000] = lambda x,y,z: 200
    data.bdrycond.fct[3000] = lambda x,y,z: 320
    #postprocess
    data.postproc.set(name='bdrymean_right', type='bdry_mean', colors=1001)
    data.postproc.set(name='bdrymean_left', type='bdry_mean', colors=1003)
    data.postproc.set(name='bdrymean_up', type='bdry_mean', colors=1002)
    data.postproc.set(name='bdrynflux', type='bdry_nflux', colors=[3000])
    data.postproc.set(name='pointvalue', type='pointvalues', colors=9999)
    # data.postproc.set(name='linemean', type='linemeans', colors=999)
    #paramaters in equation
    # cell-wise
    # data.params.set_scal_cells("kheat", [100], 0.001)
    # data.params.set_scal_cells("kheat", [200], 10.0)
    # fct-wise
    def kheat(color, x, y, z):
        if color == 100: return 0.001
        return 100
    data.params.fct_glob["kheat"] = kheat
    if convection: data.params.fct_glob["convection"] = ["0", "0.001"]
    if mode=='dynamic': data.params.fct_glob["initial_condition"] = "200"
    return data

# ================================================================c#

main(mode='static', convection=True, h=1)
# main(mode='dynamic', convection=True, h=0.1)