var React = require("react");
var MyComponent = require("../src/components/Article/Article");
var TestUtils = React.addons.TestUtils;


describe ('hello world' , () =>{
       /* it('hello world', function(){
            var zone= <ZoneRisque /> ;
            ReactTestUtils.renderIntoDocument(zone)
        });*/
        beforeEach(function() {
            instance = TestUtils.renderIntoDocument(<MyComponent>Some text</MyComponent>);
          });
      
          it("Check Text Assignment", function() {
           // expect(instance.refs.p).toBeDefined();
           // expect(instance.refs.p.props.children).toBe("Some text");
          });
   
});