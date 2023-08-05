#ifndef FILE_OCCGEOM
#define FILE_OCCGEOM

/* *************************************************************************/
/* File:   occgeom.hpp                                                     */
/* Author: Robert Gaisbauer                                                */
/* Date:   26. May  03                                                     */
/* *************************************************************************/

#ifdef OCCGEOMETRY

#include <meshing.hpp>

#include <Standard_Version.hxx>
#include "BRep_Tool.hxx"
#include "Geom_Curve.hxx"
#include "Geom2d_Curve.hxx"
#include "Geom_Surface.hxx"
#include "GeomAPI_ProjectPointOnSurf.hxx"
#include "GeomAPI_ProjectPointOnCurve.hxx"
#include "BRepTools.hxx"
#include "TopExp.hxx"
#include "BRepBuilderAPI_MakeVertex.hxx"
#include "BRepBuilderAPI_MakeShell.hxx"
#include "BRepBuilderAPI_MakeSolid.hxx"
#include "BRepOffsetAPI_Sewing.hxx"
#include "BRepLProp_SLProps.hxx"
#include "BRepAdaptor_Surface.hxx"
#include "Poly_Triangulation.hxx"
#include "Poly_Array1OfTriangle.hxx"
#include "TColgp_Array1OfPnt2d.hxx"
#include "Poly_Triangle.hxx"
#include "GProp_GProps.hxx"
#include "BRepGProp.hxx"
#include "gp_Pnt.hxx"
#include "TopoDS.hxx"
#include "TopoDS_Solid.hxx"
#include "TopExp_Explorer.hxx"
#include "TopTools_ListIteratorOfListOfShape.hxx"
#include "TopoDS_Wire.hxx"
#include "BRepTools_WireExplorer.hxx"
#include "TopTools_IndexedMapOfShape.hxx"
#include "BRepLProp_CLProps.hxx"
#include "BRepAdaptor_Curve.hxx"
#include "TopoDS_Shape.hxx"
#include "TopoDS_Face.hxx"
#include "IGESToBRep_Reader.hxx"
#include "Interface_Static.hxx"
#include "GeomAPI_ExtremaCurveCurve.hxx"
#include "Standard_ErrorHandler.hxx"
#include "Standard_Failure.hxx"
#include "ShapeUpgrade_ShellSewing.hxx"
#include "ShapeFix_Shape.hxx"
#include "ShapeFix_Wireframe.hxx"
#include "BRepMesh_IncrementalMesh.hxx"
#include "BRepBndLib.hxx"
#include "Bnd_Box.hxx"
#include "ShapeAnalysis.hxx"
#include "ShapeBuild_ReShape.hxx"
#include "BOPAlgo_Builder.hxx"

// Philippose - 29/01/2009
// OpenCascade XDE Support
// Include support for OpenCascade XDE Features
#include "TDocStd_Document.hxx"
#include "Quantity_Color.hxx"
#include "XCAFApp_Application.hxx"
#include "XCAFDoc_ShapeTool.hxx"
#include "XCAFDoc_Color.hxx"
#include "XCAFDoc_ColorTool.hxx"
#include "XCAFDoc_ColorType.hxx"
#include "XCAFDoc_LayerTool.hxx"
#include "XCAFDoc_DimTolTool.hxx"
#include "XCAFDoc_MaterialTool.hxx"
#include "XCAFDoc_DocumentTool.hxx"
#include "TDF_Label.hxx"
#include "TDF_LabelSequence.hxx"
#include "STEPCAFControl_Reader.hxx"
#include "STEPCAFControl_Writer.hxx"
#include "IGESCAFControl_Reader.hxx"
#include "IGESCAFControl_Writer.hxx"

#include "IGESControl_Reader.hxx"
#include "STEPControl_Reader.hxx"
#include "IGESControl_Writer.hxx"
#include "STEPControl_Writer.hxx"

#include <StepRepr_ValueRepresentationItem.hxx>
#include <StepRepr_IntegerRepresentationItem.hxx>
#include <StepRepr_CompoundRepresentationItem.hxx>
#include <StepBasic_MeasureValueMember.hxx>

#include "StlAPI_Writer.hxx"
#include "STEPControl_StepModelType.hxx"

#if OCC_VERSION_MAJOR>=7 && OCC_VERSION_MINOR>=4
#define OCC_HAVE_HISTORY
#endif




namespace netgen
{
#include "occmeshsurf.hpp"

  // extern DLL_HEADER MeshingParameters mparam;

#define PROJECTION_TOLERANCE 1e-10

#define ENTITYISVISIBLE 1
#define ENTITYISHIGHLIGHTED 2
#define ENTITYISDRAWABLE 4

#define OCCGEOMETRYVISUALIZATIONNOCHANGE   0
#define OCCGEOMETRYVISUALIZATIONFULLCHANGE 1  // Compute transformation matrices and redraw
#define OCCGEOMETRYVISUALIZATIONHALFCHANGE 2  // Redraw


  inline Point<3> occ2ng (const gp_Pnt & p)
  {
    return Point<3> (p.X(), p.Y(), p.Z());
  }

  inline Point<2> occ2ng (const gp_Pnt2d & p)
  {
    return Point<2> (p.X(), p.Y());
  }
  
  inline Vec<3> occ2ng (const gp_Vec & v)
  {
    return Vec<3> (v.X(), v.Y(), v.Z());
  }

  inline gp_Pnt ng2occ (const Point<3> & p)
  {
    return gp_Pnt(p(0), p(1), p(2));
  }

  

  class EntityVisualizationCode
  {
    int code;

  public:

    EntityVisualizationCode()
    {  code = ENTITYISVISIBLE + !ENTITYISHIGHLIGHTED + ENTITYISDRAWABLE;}

    int IsVisible ()
    {  return code & ENTITYISVISIBLE;}

    int IsHighlighted ()
    {  return code & ENTITYISHIGHLIGHTED;}

    int IsDrawable ()
    {  return code & ENTITYISDRAWABLE;}

    void Show ()
    {  code |= ENTITYISVISIBLE;}

    void Hide ()
    {  code &= ~ENTITYISVISIBLE;}

    void Highlight ()
    {  code |= ENTITYISHIGHLIGHTED;}

    void Lowlight ()
    {  code &= ~ENTITYISHIGHLIGHTED;}

    void SetDrawable ()
    {  code |= ENTITYISDRAWABLE;}

    void SetNotDrawable ()
    {  code &= ~ENTITYISDRAWABLE;}
  };



  class Line
  {
  public:
    Point<3> p0, p1;
    double Dist (Line l);
    double Length () { return (p1-p0).Length(); }
  };
  


  inline double Det3 (double a00, double a01, double a02,
                      double a10, double a11, double a12,
                      double a20, double a21, double a22)
  {
    return a00*a11*a22 + a01*a12*a20 + a10*a21*a02 - a20*a11*a02 - a10*a01*a22 - a21*a12*a00;
  }
  
  class DLL_HEADER OCCParameters
  {
  public:

    /// Factor for meshing close edges, moved to meshingparameters
    // double resthcloseedgefac = 2.;

    /// Enable / Disable detection of close edges
    // int resthcloseedgeenable = true;

    /// Minimum edge length to be used for dividing edges to mesh points
    double resthminedgelen = 0.001;

    /// Enable / Disable use of the minimum edge length (by default use 1e-4)
    int resthminedgelenenable = true;

    /*!
      Dump all the OpenCascade specific meshing parameters 
      to console
    */
    void Print (ostream & ost) const;
  };


  class ShapeProperties
  {
  public:
    optional<string> name;
    optional<Vec<4>> col;
    double maxh = 1e99;
    double hpref = 0;  // number of hp refinement levels (will be multiplied by factor later)
    void Merge(const ShapeProperties & prop2)
    {
      if (prop2.name) name = prop2.name;
      if (prop2.col) col = prop2.col;
      maxh = min2(maxh, prop2.maxh);
    }
  };


  class OCCIdentification
  {
  public:
    TopoDS_Shape other;
    Transformation<3> trafo;
    bool inverse;
    string name;
  };


  class MyExplorer
  {
    class Iterator
    {
      TopExp_Explorer exp;
    public:
      Iterator (TopoDS_Shape ashape, TopAbs_ShapeEnum atoFind, TopAbs_ShapeEnum atoAvoid)
        : exp(ashape, atoFind, atoAvoid) { }
      auto operator*() { return exp.Current(); }
      Iterator & operator++() { exp.Next(); return *this; }
      bool operator!= (nullptr_t nu) { return exp.More(); }
    };

  public:
    TopoDS_Shape shape;
    TopAbs_ShapeEnum toFind;
    TopAbs_ShapeEnum toAvoid;
    MyExplorer (TopoDS_Shape ashape, TopAbs_ShapeEnum atoFind, TopAbs_ShapeEnum atoAvoid = TopAbs_SHAPE)
      : shape(ashape), toFind(atoFind), toAvoid(atoAvoid) { ; }
    Iterator begin() { return Iterator(shape, toFind, toAvoid); }
    auto end() { return nullptr; }
  };

  inline auto Explore (TopoDS_Shape shape, TopAbs_ShapeEnum toFind, TopAbs_ShapeEnum toAvoid = TopAbs_SHAPE)
  {
    return MyExplorer (shape, toFind, toAvoid);
  }

  
  class IndexMapIterator
  {
    class Iterator
    {
      const TopTools_IndexedMapOfShape & indmap;
      int i;
    public:
      Iterator (const TopTools_IndexedMapOfShape & aindmap, int ai)
        : indmap(aindmap), i(ai) { ; }
      auto operator*() { return tuple(i, indmap(i)); }
      Iterator & operator++() { i++; return *this; }
      bool operator!= (const Iterator & i2) { return i != i2.i; }
    };

  public:
    const TopTools_IndexedMapOfShape & indmap;
    IndexMapIterator (const TopTools_IndexedMapOfShape & aindmap) : indmap(aindmap) { }
    Iterator begin() { return Iterator(indmap, 1); }
    Iterator end() { return Iterator(indmap, indmap.Extent()+1); }
  };
  
  inline auto Enumerate (const TopTools_IndexedMapOfShape & indmap)
  {
    return IndexMapIterator(indmap);
  }

  
  class DLL_HEADER OCCGeometry : public NetgenGeometry
  {
    Point<3> center;
    OCCParameters occparam;
  public:
    static std::map<Handle(TopoDS_TShape), ShapeProperties> global_shape_properties;
    static std::map<Handle(TopoDS_TShape), std::vector<OCCIdentification>> identifications;

    TopoDS_Shape shape;
    TopTools_IndexedMapOfShape fmap, emap, vmap, somap, shmap, wmap;
    NgArray<bool> fsingular, esingular, vsingular;
    Box<3> boundingbox;

    // should we use 1-based arrays (JS->MH) ? 
    Array<ShapeProperties*> fprops, eprops, sprops; // pointers to the gobal property map

    mutable int changed;
    mutable NgArray<int> facemeshstatus;

    // Philippose - 15/01/2009
    // Maximum mesh size for a given face
    // (Used to explicitly define mesh size limits on individual faces)
    NgArray<double> face_maxh;
     
    // Philippose - 14/01/2010
    // Boolean array to detect whether a face has been explicitly modified 
    // by the user or not
    NgArray<bool> face_maxh_modified;
     
    // Philippose - 15/01/2009
    // Indicates which faces have been selected by the user in geometry mode
    // (Currently handles only selection of one face at a time, but an array would
    //  help to extend this to multiple faces)
    NgArray<bool> face_sel_status;
     
    NgArray<EntityVisualizationCode> fvispar, evispar, vvispar;
     
    double tolerance;
    bool fixsmalledges;
    bool fixspotstripfaces;
    bool sewfaces;
    bool makesolids;
    bool splitpartitions;

    int occdim = 3; // meshing is always done 3D, changed to 2D later of occdim=2
     
    OCCGeometry()
    {
      somap.Clear();
      shmap.Clear();
      fmap.Clear();
      wmap.Clear();
      emap.Clear();
      vmap.Clear();
    }

    OCCGeometry(const TopoDS_Shape& _shape, int aoccdim = 3, bool copy = false);

    Mesh::GEOM_TYPE GetGeomType() const override
    { return Mesh::GEOM_OCC; }

    void SetOCCParameters(const OCCParameters& par)
    { occparam = par; }

    void Analyse(Mesh& mesh,
                 const MeshingParameters& mparam) const override;
    void FindEdges(Mesh& mesh,
                   const MeshingParameters& mparam) const override;
    void MeshSurface(Mesh& mesh,
                     const MeshingParameters& mparam) const override;
 
    void FinalizeMesh(Mesh& mesh) const override;
     
    void Save (string filename) const override;
     
    void DoArchive(Archive& ar) override;

    PointGeomInfo ProjectPoint(int surfind, Point<3> & p) const override;
    void ProjectPointEdge (int surfind, int surfind2, Point<3> & p,
                           EdgePointGeomInfo* gi = nullptr) const override;
    bool ProjectPointGI (int surfind, Point<3> & p, PointGeomInfo & gi) const override;
    Vec<3> GetNormal(int surfind, const Point<3> & p, const PointGeomInfo* gi) const override;
    bool CalcPointGeomInfo(int surfind, PointGeomInfo& gi, const Point<3> & p3) const override;

    void PointBetweenEdge(const Point<3> & p1, const Point<3> & p2, double secpoint,
                          int surfi1, int surfi2, 
                          const EdgePointGeomInfo & ap1, 
                          const EdgePointGeomInfo & ap2,
                          Point<3> & newp, EdgePointGeomInfo & newgi) const override;
    void PointBetween(const Point<3> & p1, const Point<3> & p2, double secpoint,
                      int surfi, 
                      const PointGeomInfo & gi1, 
                      const PointGeomInfo & gi2,
                      Point<3> & newp, PointGeomInfo & newgi) const override;

    void BuildFMap();

    auto GetShape() const { return shape; }
    Box<3> GetBoundingBox() const
    { return boundingbox; }

    int NrSolids() const
    { return somap.Extent(); }

    // Philippose - 17/01/2009
    // Total number of faces in the geometry
    int NrFaces() const
    { return fmap.Extent(); }

    void SetCenter()
    { center = boundingbox.Center(); }

    Point<3> Center() const
    { return center; }

    OCCSurface GetSurface (int surfi)
    {
      cout << "OCCGeometry::GetSurface using PLANESPACE" << endl;
      return OCCSurface (TopoDS::Face(fmap(surfi)), PLANESPACE);
    }

    void CalcBoundingBox ();
    void BuildVisualizationMesh (double deflection);
    
    void RecursiveTopologyTree (const TopoDS_Shape & sh,
                                stringstream & str,
                                TopAbs_ShapeEnum l,
                                bool free,
                                const char * lname);

    void GetTopologyTree (stringstream & str);

    void PrintNrShapes ();

    void CheckIrregularEntities (stringstream & str);

    void SewFaces();

    void MakeSolid();

    void HealGeometry();
    void GlueGeometry();

    // Philippose - 15/01/2009
    // Sets the maximum mesh size for a given face
    // (Note: Local mesh size limited by the global max mesh size)
    void SetFaceMaxH(int facenr, double faceh, const MeshingParameters & mparam)
    {
      if((facenr> 0) && (facenr <= fmap.Extent()))
        {
          face_maxh[facenr-1] = min(mparam.maxh,faceh);
            
          // Philippose - 14/01/2010
          // If the face maxh is greater than or equal to the 
          // current global maximum, then identify the face as 
          // not explicitly controlled by the user any more
          if(faceh >= mparam.maxh)
            {
              face_maxh_modified[facenr-1] = 0;
            }
          else
            {
              face_maxh_modified[facenr-1] = 1;
            }
        }
    }

    void SetFaceMaxH(size_t facenr, double faceh)
    {
      if(facenr >= fmap.Extent())
        throw RangeException("OCCGeometry faces", facenr, 0, fmap.Extent());
      face_maxh[facenr] = faceh;
      face_maxh_modified[facenr] = true;
    }

    // Philippose - 15/01/2009
    // Returns the local mesh size of a given face
    double GetFaceMaxH(int facenr)
    {
      if((facenr> 0) && (facenr <= fmap.Extent()))
        {
          return face_maxh[facenr-1];
        }
      else
        {
          return 0.0;
        }
    }
      
    // Philippose - 14/01/2010
    // Returns the flag whether the given face 
    // has a mesh size controlled by the user or not
    bool GetFaceMaxhModified(int facenr)
    {
      return face_maxh_modified[facenr-1];
    }
      
    // Philippose - 17/01/2009
    // Returns the index of the currently selected face
    int SelectedFace()
    {
      for(int i = 1; i <= fmap.Extent(); i++)
        {
          if(face_sel_status[i-1])
            {
              return i;
            }
        }

      return 0;
    }

    // Philippose - 17/01/2009
    // Sets the currently selected face
    void SetSelectedFace(int facenr)
    {
      face_sel_status = 0;

      if((facenr >= 1) && (facenr <= fmap.Extent()))
        {
          face_sel_status[facenr-1] = 1;
        }
    }

    void LowLightAll()
    {
      for (int i = 1; i <= fmap.Extent(); i++)
        fvispar[i-1].Lowlight();
      for (int i = 1; i <= emap.Extent(); i++)
        evispar[i-1].Lowlight();
      for (int i = 1; i <= vmap.Extent(); i++)
        vvispar[i-1].Lowlight();
    }

    void GetUnmeshedFaceInfo (stringstream & str);
    void GetNotDrawableFaces (stringstream & str);
    bool ErrorInSurfaceMeshing ();

    //      void WriteOCC_STL(char * filename);

  private:
    bool FastProject (int surfi, Point<3> & ap, double& u, double& v) const;
  };
   

  void PrintContents (OCCGeometry * geom);

  DLL_HEADER OCCGeometry * LoadOCC_IGES (const char * filename);
  DLL_HEADER OCCGeometry * LoadOCC_STEP (const char * filename);
  DLL_HEADER OCCGeometry * LoadOCC_BREP (const char * filename);

  // Philippose - 31.09.2009
  // External access to the mesh generation functions within the OCC
  // subsystem (Not sure if this is the best way to implement this....!!)
  DLL_HEADER extern void OCCSetLocalMeshSize(const OCCGeometry & geom, Mesh & mesh, const MeshingParameters & mparam,
                                             const OCCParameters& occparam);

  DLL_HEADER extern void OCCMeshSurface (const OCCGeometry & geom, Mesh & mesh, const MeshingParameters & mparam);

  DLL_HEADER extern void OCCOptimizeSurface (OCCGeometry & geom, Mesh & mesh, const MeshingParameters & mparam);

  DLL_HEADER extern void OCCFindEdges (const OCCGeometry & geom, Mesh & mesh, const MeshingParameters & mparam);


  namespace step_utils
  {
      inline Handle(TCollection_HAsciiString) MakeName (string s)
      {
          return new TCollection_HAsciiString(s.c_str());
      };

      inline Handle(StepRepr_RepresentationItem) MakeInt (int n, string name = "")
      {
          Handle(StepRepr_IntegerRepresentationItem) int_obj = new StepRepr_IntegerRepresentationItem;
          int_obj->Init(MakeName(name), n);
          return int_obj;
      }

      inline int ReadInt (Handle(StepRepr_RepresentationItem) item)
      {
          return Handle(StepRepr_IntegerRepresentationItem)::DownCast(item)->Value();
      }

      inline Handle(StepRepr_RepresentationItem) MakeReal (double val, string name = "")
      {
            Handle(StepBasic_MeasureValueMember) value_member = new StepBasic_MeasureValueMember;
            value_member->SetReal(val);
            Handle(StepRepr_ValueRepresentationItem) value_repr = new StepRepr_ValueRepresentationItem;
            value_repr->Init(MakeName(name), value_member);
            return value_repr;
      }

      inline double ReadReal (Handle(StepRepr_RepresentationItem) item)
      {
          return Handle(StepRepr_ValueRepresentationItem)::DownCast(item)
              ->ValueComponentMember()->Real();
      }


      inline Handle(StepRepr_RepresentationItem) MakeCompound( FlatArray<Handle(StepRepr_RepresentationItem)> items, string name = "" )
      {
            Handle(StepRepr_HArray1OfRepresentationItem) array_repr = new StepRepr_HArray1OfRepresentationItem(1,items.Size());

            for(auto i : Range(items))
                array_repr->SetValue(i+1, items[i]);

            Handle(StepRepr_CompoundRepresentationItem) comp = new StepRepr_CompoundRepresentationItem;
            comp->Init( MakeName(name), array_repr );
            return comp;
      }

      void WriteIdentifications(const Handle(Interface_InterfaceModel) model, const TopoDS_Shape & shape, const Handle(Transfer_FinderProcess) finder);
      void ReadIdentifications(Handle(StepRepr_RepresentationItem) item, Handle(Transfer_TransientProcess) transProc);

      inline Quantity_ColorRGBA MakeColor(const Vec<4> & c)
      {
          return Quantity_ColorRGBA (c[0], c[1], c[2], c[3]);
      }

      inline Vec<4> ReadColor (const Quantity_ColorRGBA & c)
      {
          auto rgb = c.GetRGB();
          return {rgb.Red(), rgb.Green(), rgb.Blue(), c.Alpha()};
      }


      void LoadProperties(const TopoDS_Shape & shape,
                          const STEPCAFControl_Reader & reader,
                          const Handle(TDocStd_Document) step_doc);
      void WriteProperties(const Handle(Interface_InterfaceModel) model, const Handle(Transfer_FinderProcess) finder, const TopoDS_Shape & shape);

      void WriteSTEP(const TopoDS_Shape & shape, string filename);

      inline void WriteSTEP(const OCCGeometry & geo, string filename)
      {
          WriteSTEP(geo.GetShape(), filename);
      }

      // deep copy, also ensures consistent shape ordering (face numbers etc.)
      TopoDS_Shape WriteAndRead(const TopoDS_Shape shape);
  } // namespace step_utils
}

#endif

#endif
