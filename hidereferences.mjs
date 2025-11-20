/**
 * MyST Plugin to hide auto-generated references sections
 */

/**
 * Transform to remove references sections from the document tree
 * 
 * @param {object} opts - options (unused)
 * @param {object} utils - utility functions provided by MyST
 */
function hideReferencesTransform(opts, utils) {
  return (mdast) => {
    // Find all sections with id="references"
    const referenceSections = utils.selectAll('section[identifier=references]', mdast);
    
    // Remove each references section
    referenceSections.forEach((node) => {
      // Find the parent of this node
      utils.remove(node);
    });
    
    // Alternative approach: Find by checking children for "References" header
    utils.selectAll('section', mdast).forEach((section) => {
      // Check if this section has a heading child with text "References"
      const heading = section.children?.find(
        (child) => child.type === 'heading' && 
        child.children?.some(
          (grandchild) => grandchild.type === 'text' && 
          grandchild.value === 'References'
        )
      );
      
      if (heading) {
        utils.remove(section);
      }
    });
  };
}

// Register the transform to run at the document stage
const hideReferencesTransformPlugin = {
  plugin: hideReferencesTransform,
  stage: 'document',
};

/**
 * Export the plugin
 */
const plugin = {
  name: 'Hide References Section',
  author: 'Custom',
  license: 'MIT',
  transforms: [hideReferencesTransformPlugin],
};

export default plugin;
